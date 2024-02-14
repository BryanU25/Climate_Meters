from flask import Blueprint, render_template, request, redirect, jsonify
from backend.models.Categorias import *
from backend.models.C_liqui import CombustiblesLiquidos
from backend.models.C_solid import CombustiblesSolidos
from backend.models.Catalogos import *
from backend.database.db import db
from backend.models.Schemas import *



HC_admins = Blueprint("HC_admins", __name__)


def Errores_JSON(Cod, Dato):
    if Cod == 600:
        return (
            jsonify(
                {
                    "success": False,
                    "error": "La categoria asignada no contiene una 'class' modelo equivalente",
                    "categoria": Dato,
                }
            ),
            600,
        )
    elif Cod == 601:
        return (
            jsonify(
                {
                    "success": False,
                    "error": "La categoria especificada no esta referenciada en la tabla catalogo_categorias",
                    "categoria": Dato,
                }
            ),
            601,
        )


def Success_JSON(Cod, Dato):
    if Cod == 210:
        return (
            jsonify(
                {
                    "success": True,
                    "message": "Datos guardados correctamente",
                    "Dato": Dato,
                }
            ),
            210,
        )
    elif Cod == 211:
        return (
            jsonify(
                {
                    "success": True,
                    "message": "Datos numericos modificados",
                    "Dato": Dato,
                }
            ),
            211,
        )
    elif Cod == 212:
        return (
            jsonify(
                {
                    "success": True,
                    "message": "Instancia editada",
                    "Dato": Dato,
                }
            ),
            212,
        )
    elif Cod == 213:
        return (
            jsonify(
                {
                    "success": True,
                    "message": "Instancia antigua modificada",
                    "Dato eliminado": Dato[1],
                    "Dato modificado": Dato[0],
                }
            ),
            213,
        )
    elif Cod == 214:
        return (
            jsonify(
                {
                    "success": True,
                    "message": "Instancia ingresada en nueva categoria",
                    "Dato eliminado": Dato[1],
                    "Dato ingresado": Dato[0],
                }
            ),
            214,
        )
    elif Cod == 215:
        return (
            jsonify(
                {
                    "succes": True,
                    "message": "Dato eliminado correctamente",
                    "Dato": Dato,
                }
            ),
            215,
        )


@HC_admins.route("/Admin/CargaAmb")
def Adm_CargaAmb():
    try:
        Datos = {}
        Modelos = (
            CatalogoCategorias.query.all()
        )  # Obtención de cada fila del Catalogo de Categorias

        for Modelo in Modelos:
            Modelo_Categoria = globals().get(
                Modelo.clase_modelo
            )  # Obtención de todas las "clases modelo" según el nombre
            if Modelo_Categoria:
                InstanciasXCategoria = Modelo_Categoria.query.all()
                Datos[Modelo.nombre_categoria] = [
                    InstanciaSchema().dump(Instancia)
                    for Instancia in InstanciasXCategoria
                ]

        # Si la solicitud espera JSON o no especifica un formato, responde con JSON
        # if 'application/json' in request.accept_mimetypes:
        if request.headers.get("Accept") == "application/json":
            return jsonify(Datos)
        else:
            return render_template("/admin/CargaAmb.html", datos=Datos)
    except Exception as ex:
        return jsonify({"error": "No se pudo consultar la base de datos"}), 500


@HC_admins.route("/Admin/CargaAmb/Guardar", methods=["POST"])
def Adm_CargaAmb_Guardar():
    
    try:
        Dato = request.get_json()

        Categoria = Dato.pop("Sel_Categoria")
        Unidad = Dato.pop("Sel_Unidad")
        Esquema_Instancia = InstanciaSchema().load(Dato)

        Id_Catego = Categorias.buscar_por_nombre(
            Categoria
        ).idCategorias  # Obtención de la Id de la categoria a partir del nombre

        categoria_catalogo = CatalogoCategorias.query.filter_by(
            nombre_categoria=Categoria
        ).first()  # Obtención del nombre de la clase modelo

        if categoria_catalogo:
            modelo_categoria = globals().get(
                categoria_catalogo.clase_modelo
            )  # Obtención de la clase de modelo según el nombre

            if modelo_categoria:
                # Crear una instancia
                componente = modelo_categoria(
                    **Esquema_Instancia,
                    Categorias_idCategorias=Id_Catego,
                )
                print (componente)

                # Inserción en la tabla correspondiente
                db.session.add(componente)
                db.session.commit()

                return Success_JSON(210, Dato)
            else:
                return Errores_JSON(600, modelo_categoria)
        else:
            return Errores_JSON(601, categoria_catalogo)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@HC_admins.route("/Admin/CargaAmb/Editar", methods=["PUT"])
def Adm_CargaAmb_Edit():
    try:
        Dato = request.get_json()        
        new_Nombre = Dato.pop("New_Name")
        old_Nombre = Dato.pop("Old_Name")  # creo que no me interesa
        old_Categoria = Dato.pop("Old_Categoria")
        new_Categoria = Dato.pop("New_Categoria")
        id = Dato.pop("id")
        
        categoria_catalogo_nuevo = CatalogoCategorias.query.filter_by(
            nombre_categoria=new_Categoria
        ).first()  # Obtención del nombre de la clase modelo

        if categoria_catalogo_nuevo:
            modelo_categoria_nuevo = globals().get(
                categoria_catalogo_nuevo.clase_modelo
            )  # Obtención de la clase de modelo según el nombre

            if modelo_categoria_nuevo:
                if old_Categoria == new_Categoria:
                    # Consulta id Instancia
                    Instancia = modelo_categoria_nuevo.buscar_por_id(id)
                    Serial = InstanciaSchema().dump(Instancia)
                    if modelo_categoria_nuevo.query.filter_by(
                        Nombre=new_Nombre
                    ).first():
                        for key, value in Dato.items():
                            if hasattr(Instancia, key):
                                setattr(Instancia, key, value)
                        db.session.commit()

                        return Success_JSON(211, Serial)
                    else:
                        Instancia.Nombre = new_Nombre
                        for key, value in Dato.items():
                            if hasattr(Instancia, key):
                                setattr(Instancia, key, value)
                        db.session.commit()

                        return Success_JSON(212, Serial)
                else:  # Caso donde se debe borrar de tabla antigua e ingresar en una tabla nueva (Cambio de categoria)
                    Catego = Categorias.buscar_por_nombre(
                        new_Categoria
                    )  # Obtención de la categoría deseada

                    Id_Catego = (
                        Catego.idCategorias
                    )  # Obtención de la Id de la categoria

                    categoria_catalogo_viejo = CatalogoCategorias.query.filter_by(
                        nombre_categoria=old_Categoria
                    ).first()  # Obtención del nombre de la clase modelo antigua

                    if categoria_catalogo_viejo:
                        modelo_categoria_viejo = globals().get(
                            categoria_catalogo_viejo.clase_modelo
                        )  # Obtención de la clase de modelo antigua según el nombre

                        if modelo_categoria_viejo:
                            Instancia_Old = modelo_categoria_viejo.buscar_por_id(id)
                            Serial_Viejo = InstanciaSchema().dump(Instancia_Old)                            

                            db.session.delete(Instancia_Old)
                            db.session.commit()

                            if modelo_categoria_nuevo.query.filter_by(
                                Nombre=new_Nombre
                            ).first():
                                Instancia_Nueva = (
                                    modelo_categoria_nuevo.buscar_por_nombre(new_Nombre)
                                )
                                Serial_Nuevo = InstanciaSchema().dump(Instancia_Nueva)
                                print(
                                    "Asegurar si desea modificar sobre una instancia ya existente"
                                )
                                for key, value in Dato.items():
                                    if hasattr(Instancia_Nueva, key):
                                        setattr(Instancia_Nueva, key, value)
                                db.session.commit()

                                return Success_JSON(213, [Serial_Nuevo, Serial_Viejo])
                            else:
                                componente = modelo_categoria_nuevo(
                                    Nombre=new_Nombre,
                                    **Dato,
                                    Categorias_idCategorias=Id_Catego,
                                )
                                Serial_Nuevo = InstanciaSchema().dump(componente)
                                db.session.add(componente)
                                db.session.commit()

                                return Success_JSON(214, [Serial_Nuevo, Serial_Viejo])
                        else:
                            return Errores_JSON(600, modelo_categoria_viejo)
                    else:
                        return Errores_JSON(601, categoria_catalogo_viejo)
            else:
                return Errores_JSON(600, modelo_categoria_nuevo)
        else:
            return Errores_JSON(601, categoria_catalogo_nuevo)        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@HC_admins.route("/Admin/CargaAmb/Borrar", methods=["DELETE"])
def Adm_CargaAmb_Delete():
    try:
        Dato = request.get_json()        
        Id = Dato["id"]
        Categoria = Dato["Categoria"]        
        
        categoria_catalogo = CatalogoCategorias.query.filter_by(
            nombre_categoria=Categoria
        ).first()  # Obtención del nombre de la clase modelo

        if categoria_catalogo:
            modelo_categoria = globals().get(
                categoria_catalogo.clase_modelo
            )  # Obtención de la clase de modelo según el nombre

            if modelo_categoria:
                Instancia = modelo_categoria.buscar_por_id(Id)
                Serial = InstanciaSchema().dump(Instancia)
                db.session.delete(Instancia)
                db.session.commit()
                return Success_JSON(215, Serial)
            else:
                return Errores_JSON(600, modelo_categoria)
        else:
            return Errores_JSON(601, categoria_catalogo)
    except Exception as e:
        return jsonify({"succes": False, "error": "El dato no se logro borrar"})

from flask import Blueprint, render_template, request, redirect, jsonify
from backend.database.db import db
from datetime import datetime
from backend.models.Formularios import HuellaCarbonoForm
from backend.models.Categorias import Categorias
from backend.models.HC_Generada import *
from backend.models.Catalogos import *
from flask_wtf.csrf import validate_csrf

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
                    "message": "Datos guardaos correctamente",
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

def Suma_Datos(Datos):
    Suma = 0
    for dato in Datos:
        Suma = dato + Suma
    return Suma


def CO2_e(Factores, Datos):
    CO2 = (Datos * Factores["CO2"]) / 1000
    CH4_F = (Datos * Factores["CH4_F"]) / 1000
    N2O_F = (Datos * Factores["N2O_F"]) / 1000
    CH4_M = (Datos * Factores["CH4_M"]) / 1000
    N2O_M = (Datos * Factores["N2O_M"]) / 1000
    CO2equi = CO2 + (CH4_F * 28) + (N2O_F * 265) + (CH4_M * 28) + (N2O_M * 265)
    return CO2equi


HuellaCarbono = Blueprint("HuellaCarbono", __name__)


@HuellaCarbono.route("/")
def sitio():
    return render_template("site/index.html")


@HuellaCarbono.route("/Cliente/Informacion")
def resumen():
    return render_template("client/Informacion.html")


@HuellaCarbono.route("/Cliente/HC_Calculada", methods=["GET"])
def HC_Calculado():
    Instancia = []
    Cant_Datos = list(range(1, 13))
    # Identificar el ID de usuario y
    Calculos = HuellaGenerada.query.filter_by(User_ID=1).all()
    Instancia = [HuellaGeneradaEsquema().dump(Calculo) for Calculo in Calculos]

    Existentes = Categorias.query.all()
    if Existentes is not None:
        form = HuellaCarbonoForm()
        form.Sel_Categoria.choices = [(Categoria.Nombre) for Categoria in Existentes]
        form.Sel_Datos.choices = [(Dato) for Dato in Cant_Datos]

        if request.headers.get("Accept") == "application/json":
            # Usa jsonify para convertir la lista de registros en formato JSON
            return jsonify(Instancia)
        else:
            return render_template(
                "client/Huella_Carbono.html", Cal_Existen=Calculos, form=form
            )

    else:
        # Manejo de error si la categoría no se encuentra en el catálogo
        return render_template(
            "client/Huella_Carbono.html", {"error": "Categoría no encontrada"}
        )


@HuellaCarbono.route("/Cliente/HC_Calculada/SeleccionCategoria/<Cate_Seleccionada>")
def Categoria_Calculadora_HC(Cate_Seleccionada):
    Catego = Categorias.buscar_por_nombre(Cate_Seleccionada)
    Nombres_Fuentes = []
    if Catego is not None:
        Relacion_de_categoria = CatalogoRelaciones.obtener_relacion_de_categoria(
            Cate_Seleccionada
        )

        Registros_Relacionados = getattr(Catego, Relacion_de_categoria)
        for Registro in Registros_Relacionados:
            Nombres_Fuentes.append(Registro.Nombre)
            # Usa jsonify para convertir la lista de registros en formato JSON
    return jsonify({"Fuentes": Nombres_Fuentes})


# @HuellaCarbono.route("/Cliente/HC_Calculada/SeleccionCategoria", methods=["POST"])
# def Categoria_Calculadora_HC():
#     form = HuellaCarbonoForm()
#     if form.validate:
#     # Obtiene la categoria seleccionada en el desplegable a traves de un script JS (Dinamico)
#         # Categoria_Seleccionada = request.json.get("Categoria")
#         Catego = Categorias.buscar_por_nombre("Combustible Solido")
#         if Catego is not None:
#             Relacion_de_categoria = CatalogoRelaciones.obtener_relacion_de_categoria(
#                 "Combustible Solido"
#             )
#             print(Relacion_de_categoria)

#             Registros_Relacionados = getattr(Catego, Relacion_de_categoria)
#             form.Sel_Fuente.choices = [(Registro.Nombre) for Registro in Registros_Relacionados]
#             return render_template("client/Huella_Carbono.html", form=form)
#             # for Registro in Registros_Relacionados:
#             #     Nombres_Fuentes.append(Registro.Nombre)
#             # # Usa jsonify para convertir la lista de registros en formato JSON
#             # return jsonify(Nombres_Fuentes)
#         else:
#             # Manejo de error si la categoría no se encuentra en el catálogo
#             return jsonify({"error": "Categoría no encontrada"})
#         # Si no se valida el formulario, renderiza la plantilla con los errores
#         # return render_template('client/Huella_Carbono.html', form=form)


@HuellaCarbono.route("/Cliente/HC_Calculada/Calcular", methods=["POST"])
def Calculo_Calculadora_HC():
    try:
        data = request.get_json()        
        Cantidad = data.pop("Datos")  
        Cantidad = [int (x) for x in Cantidad]                      
        Promedio = Suma_Datos(Cantidad)        
        Categoria_Seleccionada = data.pop("Categoria")        
        Catego = Categorias.buscar_por_nombre(Categoria_Seleccionada)
        if Catego is not None:
            Relacion_De_Categoria = CatalogoRelaciones.obtener_relacion_de_categoria(
                Catego.Nombre
            )

            Fuente_Seleccionada = data.pop("Fuente")

            # Dada la categoria seleccionada se obtiene el objeto de la clase modelo
            Modelo = getattr(Categorias, Relacion_De_Categoria).property.mapper.class_
            Registro = Modelo.query.filter_by(Nombre=Fuente_Seleccionada).first()

        if Registro is not None:
            # Se obtiene el registro especifico seleccionado en "Sel_Fuente" dada la Categoria especifica "Sel_Categoria"

            if Registro is not None:
                Registros_Factores = {
                    "CO2": Registro.CO2,
                    "CH4_F": Registro.CH4_F,
                    "N2O_F": Registro.N2O_F,
                    "CH4_M": Registro.CH4_M,
                    "N2O_M": Registro.N2O_M,
                }
            CO2_equivalente = CO2_e(Registros_Factores, Promedio)

            # Obtencion de fecha actual y cambio a cadena de formato ISO 8601
            Date_Actual = datetime.now()
            Date_Format = Date_Actual.strftime("%Y-%m-%d")

            # Posterior: (Consultar ID de cliente para inserion en la DB)
            Componente = HuellaGenerada(
                User_ID=1,
                Fecha=Date_Format,
                Categoria=Categoria_Seleccionada,
                Fuente=Fuente_Seleccionada,
                Cantidad=Promedio,
                Unidad="TON",
                Generado=CO2_equivalente,
            )
            db.session.add(Componente)
            db.session.commit()        
        return Success_JSON(210, data)
        #     else:
        #         return Errores_JSON(600, modelo_categoria)
        # else:
        #     return Errores_JSON(601, categoria_catalogo)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
    # else:
    # print("Estoy en al función de Python")    
    # if request.is_json:
        # Solicitud AJAX (Content-Type: application/json)
    

    
    #     # Solicitud desde el formulario HTML
    #     try:
    #         cantidad = int(request.form["Sel_Datos"])
    #         # Resto de la lógica para el formulario HTML
    #         print("Solicitud por HTML")
    #         return redirect("/Cliente/HC_Calculada")
    #     except Exception as e:
    #         return jsonify({"status": "error", "message": str(e)}), 400

    # Se obtiene el valor de "cantidad de datos" seleccionado y se convierete en entero
    # cantidad = int(request.form["Sel_Datos"])
    # datos = []
    # # Se hace un ciclo para obtener los datos dada la cantidad de inputs ingresados (mejorable para solo recuperar donde hayan datos)
    # for dato in range(1, cantidad + 1):
    #     dato = request.form["txtDato_" + str(dato)]
    #     datos.append(int(dato))
    # Promedio = Suma_Datos(datos)

    # # Similar a la ruta "/Cliente/HC_Calculada/SeleccionCategoria" para rellenar el selector con las fuentes existentes
    # Categoria_Seleccionada = request.form["Sel_Categoria"]
    # Catego = Categorias.buscar_por_nombre(Categoria_Seleccionada)
    # if Catego is not None:
    #     Relacion_De_Categoria = CatalogoRelaciones.obtener_relacion_de_categoria(
    #         Catego.Nombre
    #     )

    #     Fuente_Seleccionada = request.form["Sel_Fuente"]

    #     # Dada la categoria seleccionada se obtiene el objeto de la clase modelo
    #     Modelo = getattr(Categorias, Relacion_De_Categoria).property.mapper.class_
    #     Registro = Modelo.query.filter_by(Nombre=Fuente_Seleccionada).first()

    #     if Registro is not None:
    #         # Se obtiene el registro especifico seleccionado en "Sel_Fuente" dada la Categoria especifica "Sel_Categoria"

    #         if Registro is not None:
    #             Registros_Factores = {
    #                 "CO2": Registro.CO2,
    #                 "CH4_F": Registro.CH4_F,
    #                 "N2O_F": Registro.N2O_F,
    #                 "CH4_M": Registro.CH4_M,
    #                 "N2O_M": Registro.N2O_M,
    #             }
    #         CO2_equivalente = CO2_e(Registros_Factores, Promedio)

    #         # Obtencion de fecha actual y cambio a cadena de formato ISO 8601
    #         Date_Actual = datetime.now()
    #         Date_Format = Date_Actual.strftime("%Y-%m-%d")

    #         # Posterior: (Consultar ID de cliente para inserion en la DB)
    #         Componente = HuellaGenerada(
    #             User_ID=1,
    #             Fecha=Date_Format,
    #             Categoria=Categoria_Seleccionada,
    #             Fuente=Fuente_Seleccionada,
    #             Cantidad=Promedio,
    #             Unidad="TON",
    #             Generado=CO2_equivalente,
    #         )
    #         db.session.add(Componente)
    #         db.session.commit()

    #     else:
    #         return print(
    #             {"error": "La fuente seleccionada no se encuentra en la base de datos"}
    #         )
    # else:
    #     # Manejo de error si la categoría no se encuentra en el catálogo
    #     return print({"error": "Categoría no encontrada"})
    # return redirect("/Cliente/HC_Calculada")


@HuellaCarbono.route("/Cliente/HC_Calculada/Editar", methods=["PUT"])
def Edicion_Calculo_HC():
    Cantidad = request.form["Edit_Text_Cantidad"]
    print(Cantidad)

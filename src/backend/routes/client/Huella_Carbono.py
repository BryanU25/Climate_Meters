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
                    "error": "La categoria solicitada no se encuentra en la base de datos",
                    "categoria": Dato,
                }
            ),
            Cod,
        )
    elif Cod == 601:
        return (
            jsonify(
                {
                    "success": False,
                    "error": "La fuente solicitada no se encuentra en la base de datos",
                    "categoria": Dato,
                }
            ),
            Cod,
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


def CO2_e(Factores, Suma):
    CO2 = (Suma * Factores["CO2"]) / 1000
    CH4_F = (Suma * Factores["CH4_F"]) / 1000
    N2O_F = (Suma * Factores["N2O_F"]) / 1000
    CH4_M = (Suma * Factores["CH4_M"]) / 1000
    N2O_M = (Suma * Factores["N2O_M"]) / 1000
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


@HuellaCarbono.route("/Cliente/HC_Calculada/Calcular", methods=["POST"])
def Calculo_Calculadora_HC():
    try:
        Data = request.get_json()

        # Calculo de suma de datos
        Cantidad = Data.pop("Datos")
        Cantidad = [int(x) for x in Cantidad]
        Promedio = Suma_Datos(Cantidad)
        #########################################

        # Se obtiene la CATEGORIA seleccionada en el formulario y procede a buscar la RELACIÓN, se obtiene el MODELO
        # segun la relación y por medio del modelo se obtienen los datos de las constantes (Registro) dada la FUENTE
        # seleccionada en el formulario
        Categoria_Seleccionada = Data.pop("Categoria")
        Catego = Categorias.buscar_por_nombre(Categoria_Seleccionada)
        if Catego is not None:
            Relacion_De_Categoria = CatalogoRelaciones.obtener_relacion_de_categoria(
                Catego.Nombre
            )

            Fuente_Seleccionada = Data.pop("Fuente")

            # Dada la categoria seleccionada se obtiene el objeto de la clase modelo
            Modelo = getattr(Categorias, Relacion_De_Categoria).property.mapper.class_
            # Se obtiene el registro especifico seleccionado en "Sel_Fuente" dada la Categoria especifica "Sel_Categoria"
            Registro = Modelo.query.filter_by(Nombre=Fuente_Seleccionada).first()

            if Registro is not None:
                Registros_Factores = vars(
                    Registro
                )  # Convierte el objeto obtenido de la base de datos en un diccionario
                CO2_equivalente = CO2_e(Registros_Factores, Promedio)

                # Obtencion de fecha actual y cambio a cadena de formato ISO 8601
                Date_Actual = datetime.now()
                Date_Format = Date_Actual.strftime("%Y-%m-%d")

                # Posterior: (Consultar ID de cliente para inserion en la DB)
                Componente = HuellaGenerada(
                    # Hacer Squema para la deserialización de los datos (datos enviados de JS a python para DB)
                    # que incluya el User_ID, Categoria, Fuente y Unidad, para posteriormente cargarlo en la DB
                    # La cantidad, La fecha y el generado son procesos en el backend (tambien se cargaran en la DB)
                    User_ID=1,
                    Categoria=Categoria_Seleccionada,
                    Fuente=Fuente_Seleccionada,
                    Unidad="TON",
                    Cantidad=Promedio,
                    Fecha=Date_Format,
                    Generado=CO2_equivalente,
                )
                db.session.add(Componente)
                db.session.commit()
                return Success_JSON(210, Data)
            else:
                return Errores_JSON(601, Fuente_Seleccionada)
        else:
            return Errores_JSON(600, Categoria_Seleccionada)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@HuellaCarbono.route("/Cliente/HC_Calculada/Editar", methods=["PUT"])
def Edicion_Calculo_HC():
    Cantidad = request.form["Edit_Text_Cantidad"]
    print(Cantidad)

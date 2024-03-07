function ObtenerDatos_Formulario_POST() {
  const Categoria = document.getElementById("Sel_Categoria").value;
  const Fuente = document.getElementById("Sel_Fuente").value;
  const Datos = parseInt(document.getElementById("Sel_Datos").value);
  const Valores = [];

  for (var i = 1; i <= Datos; i++) {
    Valores.push(document.getElementById("txtDato_" + i).value);
  }
  // # for dato in range(1, cantidad + 1):
  // #     dato = request.form["txtDato_" + str(dato)]
  // #     datos.append(int(dato))
  // # Promedio = Suma_Datos(datos)

  return {
    Categoria: Categoria,
    Fuente: Fuente,
    Datos: Valores,
  };
}

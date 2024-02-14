//(Formulario)
function ValidarDatos_Factores() {
  const datos = ObtenerDatos_Factores();
  if (
    !datos.Nombre ||
    datos.Sel_Categoria === "Seleccione una categoria" ||
    datos.Sel_Unidad === "Seleccione una unidad de medida" ||
    !datos.CO2 ||
    !datos.CH4_F ||
    !datos.N2O_F ||
    !datos.CH4_M ||
    !datos.N2O_M
  ) {
    alert("Todos los campos son obligatorios");
    return false;
  }
  return true;
}

//(Modal de Edicion)
function ValidarDatos_Edit() {
  const datosEditados = ObtenerDatos_Edit();
  if (
    !datosEditados.New_Name ||
    datosEditados.New_Categoria === "Seleccione una categoria" ||
    !datosEditados.CO2 ||
    !datosEditados.CH4_F ||
    !datosEditados.N2O_F ||
    !datosEditados.CH4_M ||
    !datosEditados.N2O_M
  ) {
    alert("Todos los campos son obligatorios");
    return false;
  }
  return true;
}

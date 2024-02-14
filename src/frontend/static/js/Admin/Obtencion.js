//Obtención (Formulario)
function ObtenerDatos_Factores() {
  const txtNombre = document.getElementById("txtNombre").value;
  const Sel_Categoria = document.getElementById("Sel_Categoria").value;
  const Sel_Unidad = document.getElementById("Sel_Unidad").value;
  const txtCO2 = document.getElementById("txtCO2").value.replace(",", ".");
  const txtCH4_Fija = document
    .getElementById("txtCH4_Fija")
    .value.replace(",", ".");
  const txtN2O_Fija = document
    .getElementById("txtN2O_Fija")
    .value.replace(",", ".");
  const txtCH4_Movil = document
    .getElementById("txtCH4_Movil")
    .value.replace(",", ".");
  const txtN2O_Movil = document
    .getElementById("txtN2O_Movil")
    .value.replace(",", ".");
  return {
    Nombre: txtNombre,
    Sel_Categoria: Sel_Categoria,
    Sel_Unidad: Sel_Unidad,
    CO2: txtCO2,
    CH4_F: txtCH4_Fija,
    N2O_F: txtN2O_Fija,
    CH4_M: txtCH4_Movil,
    N2O_M: txtN2O_Movil,
  };
}

//Obtención (Fila "Btn Edit")
function ObtenerDatos_Edit() {
  const New_Nombre = document.getElementById("Edit_Nombre").value;
  const New_Categoria = document.getElementById("Edit_Categoria").value;
  const New_CO2 = document.getElementById("Edit_CO2").value.replace(",", ".");
  const New_CH4_F = document
    .getElementById("Edit_CH4_Fija")
    .value.replace(",", ".");
  const New_N2O_F = document
    .getElementById("Edit_N2O_Fija")
    .value.replace(",", ".");
  const New_CH4_M = document
    .getElementById("Edit_CH4_Movil")
    .value.replace(",", ".");
  const New_N2O_M = document
    .getElementById("Edit_N2O_Movil")
    .value.replace(",", ".");
  return {
    New_Name: New_Nombre,
    New_Categoria: New_Categoria,
    CO2: New_CO2,
    CH4_F: New_CH4_F,
    N2O_F: New_N2O_F,
    CH4_M: New_CH4_M,
    N2O_M: New_N2O_M,
  };
}

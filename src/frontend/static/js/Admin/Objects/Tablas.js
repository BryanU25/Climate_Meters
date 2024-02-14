//Generación Filas con botones
function Gen_Filas(instancia, categoria, index) {
    var But_Edit = document.createElement("button");
    But_Edit.type = "button";
    But_Edit.id = "Edit" + index + "_" + categoria;
    But_Edit.className = "btn btn-primary";
    But_Edit.textContent = "Editar";
    var But_Delete = document.createElement("button");
    But_Delete.type = "button";
    But_Delete.id = "Delete" + index + "_" + categoria;
    But_Delete.className = "btn btn-primary";
    But_Delete.textContent = "Eliminar";
    var row =
      "<tr>" +
      '<td scope="row">' +
      instancia.Nombre +
      "</td>" +
      "<td>" +
      categoria +
      "</td>" +
      "<td>" +
      instancia.CO2 +
      "</td>" +
      "<td>" +
      instancia.CH4_F +
      "</td>" +
      "<td>" +
      instancia.N2O_F +
      "</td>" +
      "<td>" +
      instancia.CH4_M +
      "</td>" +
      "<td>" +
      instancia.N2O_M +
      "</td>" +
      "<td>" +
      "<a>" +
      But_Edit.outerHTML +
      "</a>" +
      "<a>" +
      But_Delete.outerHTML +
      "</a>" +
      "</td>" +
      "</tr>";
    return row;
  }
  
//Generación Filas Con Botones en Cliente (Filas de calculos de huella generada)
function Gen_Filas(instancia, index) {
  var But_Edit = document.createElement("button");
  But_Edit.type = "button";
  But_Edit.id = "Edit" + index;
  But_Edit.className = "btn btn-primary";
  But_Edit.textContent = "Editar";
  var But_Delete = document.createElement("button");
  But_Delete.type = "button";
  But_Delete.id = "Delete" + index;
  But_Delete.className = "btn btn-primary";
  But_Delete.textContent = "Eliminar";
  var row =
    "<tr>" +
    '<td scope="row">' +
    instancia.Fecha    +
    "</td>" +
    "<td>" +
    instancia.Categoria +
    "</td>" +
    "<td>" +
    instancia.Fuente +
    "</td>" +
    "<td>" +
    instancia.Cantidad +
    "</td>" +
    "<td>" +
    instancia.Unidad +
    "</td>" +
    "<td>" +
    instancia.Generado+
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
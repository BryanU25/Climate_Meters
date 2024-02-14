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

// document.addEventListener("DOMContentLoaded", function () {
//   // Realiza la solicitud fetch al endpoint de la API
//   console.log("Ingreso al script");
//   fetch("/Admin/CargaAmb", {
//     headers: {
//       'Accept': 'application/json', // Indica que esperamos JSON
//     },
//   })
//     .then((response) => {
//       if (!response.ok) {
//         throw new Error("Error al obtener datos de la API");
//       }
//       const contentType = response.headers.get('Content-Type');
//       if (contentType.includes('application/json')) {
//         // Si es JSON, parsea la respuesta y trabaja con los datos
//         return response.json();
//       } else {
//         // Si no es JSON, asume que es HTML y trabaja directamente con el texto
//         return response.text();
//       }
//     })
//     })
//     .then((data) => {
//         console.log("Datos recibidos:", data);
//         if (typeof data === 'object') {
//           // Si es un objeto, es JSON, itera y construye la tabla
//           for (var categoria in data) {
//             if (data.hasOwnProperty(categoria)) {
//               var instancias = data[categoria];
//               for (var i = 0; i < instancias.length; i++) {
//                 console.log("Instancias:", instancias);
//                 var instancia = instancias[i];
//                 // Agrega las filas a la tabla
//                 var row =
//                   "<tr>" +
//                   '<td scope="row">' +
//                   instancia.Nombre +
//                   "</td>" +
//                   "<td>" +
//                   categoria +
//                   "</td>" +
//                   "<td>" +
//                   instancia.CO2 +
//                   "</td>" +
//                   "<td>" +
//                   instancia.CH4_F +
//                   "</td>" +
//                   "<td>" +
//                   instancia.N2O_F +
//                   "</td>" +
//                   "<td>" +
//                   instancia.CH4_M +
//                   "</td>" +
//                   "<td>" +
//                   instancia.N2O_M +
//                   "</td>" +
//                   "<td>Editar</td>" +
//                   "</tr>";
//                 // document
//                 //   .querySelector("#Tabla1 tbody")
//                 //   .insertAdjacentHTML("beforeend", row);
//               }
//             }
//           }
//         }else {
//           // Si es una cadena, es HTML, inserta directamente en el cuerpo de la tabla
//           document.querySelector("#datatablesSimple2 tbody").innerHTML = data;
//         }
//       })
//     .catch((error) => {
//       console.error(error.message);
//     });
// });

// document.addEventListener("DOMContentLoaded", function () {
//   console.log("Ingreso al script");
//   fetch("/Admin/CargaAmb", {
//     headers: {
//       'Accept': 'application/json', // Indica que esperamos JSON
//     },
//   })
//     .then((response) => {
//       if (!response.ok) {
//         throw new Error("Error al obtener datos de la API");
//       }

//       // Verifica el tipo de contenido
//       const contentType = response.headers.get('Content-Type');
//       if (contentType.includes('application/json')) {
//         // Si es JSON, parsea la respuesta y trabaja con los datos
//         return response.json();
//       } else {
//         // Si no es JSON, asume que es HTML y trabaja directamente con el texto
//         return response.text();
//       }
//     })
//     .then((data) => {
//       console.log("Datos recibidos:", data);

//       if (typeof data === 'object') {
//         // Si es un objeto, es JSON, itera y construye la tabla
//         for (var categoria in data) {
//           if (data.hasOwnProperty(categoria)) {
//             var instancias = data[categoria];
//             for (var i = 0; i < instancias.length; i++) {
//               console.log("Instancias:", instancias);
//               var instancia = instancias[i];
//               // Agrega las filas a la tabla
//               var row =
//                 "<tr>" +
//                 '<td scope="row">' +
//                 instancia.Nombre +
//                 "</td>" +
//                 "<td>" +
//                 categoria +
//                 "</td>" +
//                 "<td>" +
//                 instancia.CO2 +
//                 "</td>" +
//                 "<td>" +
//                 instancia.CH4_F +
//                 "</td>" +
//                 "<td>" +
//                 instancia.N2O_F +
//                 "</td>" +
//                 "<td>" +
//                 instancia.CH4_M +
//                 "</td>" +
//                 "<td>" +
//                 instancia.N2O_M +
//                 "</td>" +
//                 "<td>Editar</td>" +
//                 "</tr>";
//               // document
//               //   .querySelector("#Tabla1 tbody")
//               //   .insertAdjacentHTML("beforeend", row);
//             }
//           }
//         }
//       } else {
//         // Si es una cadena, es HTML, inserta directamente en el cuerpo de la tabla
//         document.querySelector("#datatablesSimple2 tbody").innerHTML = data;
//       }
//     })
//     .catch((error) => {
//       console.error(error.message);
//     });
// });

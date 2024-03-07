//Solicitud "GET" (Rellena Tabla)
document.addEventListener("DOMContentLoaded", function () {
  fetch("/Admin/CargaAmb", {
    headers: {
      Accept: "application/json",
    },
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Error al obtener datos de la API");
      }
      const contentType = response.headers.get("Content-Type");
      if (contentType.includes("application/json")) {
        return response.json();
      } else {
        return response.text();
      }
    })
    .then((data) => {
      const tbodyElement = document.getElementById("Body_T1");
      if (tbodyElement !== null) {
        if (typeof data === "object") {
          instanciasPorCategoria = data;
          for (var categoria in data) {
            if (data.hasOwnProperty(categoria)) {
              const instancias = data[categoria];
              instancias.forEach((instancia, index) => {
                const row = Gen_Filas(instancia, categoria, index);
                tbodyElement.insertAdjacentHTML("beforeend", row);
              });
            } else {
              tbodyElement.innerHTML = data;
            }
          }
          tbodyElement.addEventListener("click", Clic_Tabla);
        }
      } else {
        console.error("No se encontró el elemento tbody");
      }
      const Tabla1 = document.getElementById("Tabla1");
      if (Tabla1) {
        new simpleDatatables.DataTable(Tabla1, {
          searchable: false,
          sortable: false,
        });
      }
    })
    .catch((error) => {
      console.error(error.message);
    });
});

//Solicitud "POST" (Boton "Guardar")
function EnviarDatos_Factores() {
  if (!ValidarDatos_Factores()) {
    throw new Error("Los datos ingresados no son validos");
  }
  const datos = ObtenerDatos_Factores();
  fetch("/Admin/CargaAmb/Guardar", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken, // Incluir el token CSRF en las cabeceras
    },
    body: JSON.stringify(datos),
  })
    .then((response) => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error("Error en la solicitud al servidor");
      }
    })
    .then(Respuesta_Servidor)
    .catch((error) => {
      console.error("Error al enviar la solicitud:", error);
    });
}

//Solicitud "PUT" (Boton "Guardar Cambios")
function Guardar_Cambios() {
  // Obtener los valores editados
  if (!ValidarDatos_Edit()) {
    throw new Error("Los datos ingresados no son validos");
  }
  const datosEditados = ObtenerDatos_Edit();
  var instanciaClicada = instanciaSeleccionada;
  var old_categoria = categoriaVieja;

  console.log(instanciaClicada.Nombre, old_categoria, datosEditados);

  // Enviar la solicitud PUT al servidor
  fetch("/Admin/CargaAmb/Editar", {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken":
        "\xa6\xa5\xdd\x1fG\xea\x16\x84\xf8K\xf2\xa5\xe5\xa8\xfe\xd4ae\x80VV\xc3*\x06",
    },
    body: JSON.stringify({
      id: instanciaClicada.id,
      Old_Categoria: old_categoria,
      Old_Name: instanciaClicada.Nombre,
      ...datosEditados,
    }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Error al editar datos en el servidor");
      }
      // Aquí puedes realizar acciones adicionales si la edición fue exitosa
    })
    .catch((error) => {
      console.error(error.message);
    })
    .finally(() => {
      // Cierra el modal después de enviar la solicitud

      editModal.hide();
      window.location.reload();
    });
}

//Solicitud "DELETE" (Boton "Confirmar")
function Confirmar_Borrado() {
  fetch("/Admin/CargaAmb/Borrar", {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken":
        "\xa6\xa5\xdd\x1fG\xea\x16\x84\xf8K\xf2\xa5\xe5\xa8\xfe\xd4ae\x80VV\xc3*\x06",
    },
    body: JSON.stringify({
      id: id_borrar,
      Categoria: categoria_borrar,
    }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Error al editar datos en el servidor");
      }
      // Aquí puedes realizar acciones adicionales si la edición fue exitosa
    })
    .catch((error) => {
      console.error(error.message);
    })
    .finally(() => {
      // Cierra el modal después de enviar la solicitud
      deleteModal.hide();
      window.location.reload();
    });
}

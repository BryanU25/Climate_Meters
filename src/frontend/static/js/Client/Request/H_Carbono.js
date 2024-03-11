//Solicitud "GET" (Rellena Tabla)
document.addEventListener("DOMContentLoaded", function () {
  fetch("/Cliente/HC_Calculada", {
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
      const Body_T1_Client = document.getElementById("Body_Client_T1");
      if (Body_T1_Client !== null) {
        if (typeof data === "object") {
          Instancias = data; //Variable que carga los datos de la DB para interactuar de manera global
          data.forEach((instancia, index) => {
            const row = Gen_Filas(instancia, index);
            Body_T1_Client.insertAdjacentHTML("beforeend", row);
          });
        } else {
          Body_T1_Client.innerHTML = data;
        }
        Body_T1_Client.addEventListener("click", Clic_Tabla_Cliente);
      } else {
        console.error("No se encontró el elemento tbody");
      }
      const Tabla2 = document.getElementById("Tabla_Client_1");
      if (Tabla2) {
        //Consultar como modificiar estilo y formato de tabla
        new simpleDatatables.DataTable(Tabla2, {
          searchable: false,
          sortable: false,
        });
      }
    })
    .catch((error) => {
      console.error(error.message);
    });
});

//Solicitud "POST" (Boton "Calcular")
function Calculo_Huella() {
  const csrfToken = document.querySelector('input[name="csrf_token"]').value;
  const datos = ObtenerDatos_Formulario_POST();

  fetch("/Cliente/HC_Calculada/Calcular", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
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
    .then (() => {      
      window.location.reload();
    })
    .catch((error) => {
      console.error("Error al enviar la solicitud:", error);
    });
}

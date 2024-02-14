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
        console.log(data);
        // const tbodyElement = document.getElementById("Body_C_T1");
        // if (tbodyElement !== null) {
        //   if (typeof data === "object") {
        //     instanciasPorCategoria = data;
        //     for (var categoria in data) {
        //       if (data.hasOwnProperty(categoria)) {
        //         const instancias = data[categoria];
        //         instancias.forEach((instancia, index) => {
        //           const row = Gen_Filas(instancia, categoria, index);
        //           tbodyElement.insertAdjacentHTML("beforeend", row);
        //         });
        //       } else {
        //         tbodyElement.innerHTML = data;
        //       }
        //     }
        //     tbodyElement.addEventListener("click", Clic_Tabla);
        //   }
        // } else {
        //   console.error("No se encontró el elemento tbody");
        // }
        // const Tabla1 = document.getElementById("Tabla1");
        // if (Tabla1) {
        //   new simpleDatatables.DataTable(Tabla1, {
        //     searchable: false,
        //     sortable: false,
        //   });
        // }
      })
      .catch((error) => {
        console.error(error.message);
      });
  });
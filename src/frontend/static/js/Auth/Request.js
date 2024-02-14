// function Register() {    
//     const datos = ObtenerDatos_Registro();
//     fetch("/Registro", {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//       },
//       body: JSON.stringify(datos),
//     })
//       .then((response) => {
//         if (response.ok) {
//           return response.json();
//         } else {
//           throw new Error("Error en la solicitud al servidor");
//         }
//       })
//       .then(Respuesta_Servidor)
//       .catch((error) => {
//         console.error("Error al enviar la solicitud:", error);
//       });
//   }
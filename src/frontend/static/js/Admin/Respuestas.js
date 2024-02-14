function Respuesta_Servidor(data){
    if (data.success) {
      alert("Datos guardados correctamente");
      window.location.reload();
    } else {
      alert("Error al guardar los datos: " + data.error);
    }
  }
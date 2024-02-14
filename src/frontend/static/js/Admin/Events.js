//Funcion que escucha "Clicks" en tablas
window.Clic_Tabla = function (event) {
    var botonClicadoId = event.target.id;
    var partes = botonClicadoId.split("_");
    var categoria = partes[1];
  
    // Verificar si el clic fue en un botón de edición o eliminación
    if (event.target.id.includes("Edit")) {
      // Obtener el ID del botón que se clicó
      var indice = partes[0].replace("Edit", "");
  
      try {
        var instanciasDeCategoria = instanciasPorCategoria[categoria];
        var instanciaClicada = instanciasDeCategoria[indice];
        instanciaSeleccionada = instanciaClicada;
        categoriaVieja = categoria;
  
        // Llenar los campos del modal con los datos de la instancia
        document.getElementById("Edit_Nombre").value = instanciaClicada.Nombre;
        document.getElementById("Edit_CO2").value = instanciaClicada.CO2;
        document.getElementById("Edit_CH4_Fija").value = instanciaClicada.CH4_F;
        document.getElementById("Edit_N2O_Fija").value = instanciaClicada.N2O_F;
        document.getElementById("Edit_CH4_Movil").value = instanciaClicada.CH4_M;
        document.getElementById("Edit_N2O_Movil").value = instanciaClicada.N2O_M;
        document.getElementById("Edit_Categoria").value = categoria;
  
        // Abrir el modal
        editModal.show();
      } catch (error) {
        console.error("No se identificó la instancia a editar:",error);
      }
    }
    else if (event.target.id.includes("Delete")){
      // Obtener el ID del botón que se clicó
      var indice = partes[0].replace("Delete", "");
  
      try {
        var instanciasDeCategoria = instanciasPorCategoria[categoria];
        var instanciaClicada = instanciasDeCategoria[indice];
        id_borrar = instanciaClicada.id;        
        categoria_borrar = categoria;     
        // Abrir el modal
        document.getElementById('Delete_Nombre').innerText = instanciaClicada.Nombre;
        document.getElementById('Delete_Categoria').innerText = categoria_borrar;
  
  
        deleteModal.show();
      } catch (error) {
        console.error("No se identificó la acción a realizar");
      }
    }
  };
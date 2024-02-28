window.Clic_Tabla_Cliente = async function (event) {
  var botonClicadoId = event.target.id;
  // Verificar si el clic fue en un botón de edición o eliminación
  if (event.target.id.includes("Edit")) {    
    // Obtener el ID del botón que se clicó
    var indice = botonClicadoId.replace("Edit", "");
    
    try {
      var InstanciaClicada = Instancias[indice];    
      // Llenar los campos del modal con los datos de la instancia
      Sel_Cate_Modal.style.display = "block";
      Sel_Cate_Modal.value = InstanciaClicada.Categoria;
      await Cambio_Selector_Fuente(Sel_Cate_Modal, Sel_Fuen_Modal);        
      Sel_Fuen_Modal.style.display = "block";
      Sel_Fuen_Modal.value = InstanciaClicada.Fuente;
      // document.getElementById("Sel_Fuente").value = InstanciaClicada.Fuente;
      // document.getElementById("Edit_CH4_Fija").value = InstanciaClicada.Cantidad;
      // document.getElementById("Edit_N2O_Fija").value = InstanciaClicada.Unidad;
      // document.getElementById("Edit_CH4_Movil").value = InstanciaClicada.Generada;

      // Abrir el modal
      Modal_Edit.show();      
    } catch (error) {
      console.error("No se identificó la instancia a editar:", error);
    }
  } else if (event.target.id.includes("Delete")) {
    // Obtener el ID del botón que se clicó
    var indice = partes[0].replace("Delete", "");

    try {
      var instanciasDeCategoria = instanciasPorCategoria[categoria];
      var instanciaClicada = instanciasDeCategoria[indice];
      id_borrar = instanciaClicada.id;
      categoria_borrar = categoria;
      // Abrir el modal
      document.getElementById("Delete_Nombre").innerText =
        instanciaClicada.Nombre;
      document.getElementById("Delete_Categoria").innerText = categoria_borrar;

      deleteModal.show();
    } catch (error) {
      console.error("No se identificó la acción a realizar");
    }
  }
};

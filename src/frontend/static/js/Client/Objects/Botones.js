document.addEventListener("DOMContentLoaded", function () {
  // Sin Condicion
  var Boton = document.getElementById("Add_Fuente");
  // var Editar = document.getElementById(
  //   "Editar" + array.forEach((element) => {})
  // );

  // Condicionados
  var Campo1 = document.getElementById("Lab_Categoria");
  var Campo2 = document.getElementById("Sel_Categoria");
  var Campo3 = document.getElementById("Lab_Fuente");
  var Campo4 = document.getElementById("Sel_Fuente");
  var Campo5 = document.getElementById("Lab_Datos");
  var Campo6 = document.getElementById("Sel_Datos");
  // var Campo7 = document.getElementById("Label_Incertumbre");
  // var Campo8 = document.getElementById("Incertidumbre");
  var Campo9 = document.getElementById("Boton_Calcular");

  accionRealizada = false;

  // Agrega un controlador de eventos al botón
  Boton.addEventListener("click", function () {
    // Muestra el selector
    Campo1.style.display = "block";
    Campo2.style.display = "block";
    Campo3.style.display = "block";
    Campo4.style.display = "block";
    Campo5.style.display = "block";
    Campo6.style.display = "block";
    // Campo7.style.display = "block";
    // Campo8.style.display = "block";
    Campo9.style.display = "block";
  });
});
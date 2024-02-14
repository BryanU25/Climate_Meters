// Obtención de objetos
let Selector_Categoria = document.getElementById("Sel_Categoria");
let Selector_Fuente = document.getElementById("Sel_Fuente");
let Selector_Datos = document.getElementById("Sel_Datos");

// Carga de valores predeterminados no seleccionables
Selector_Categoria.innerHTML += '<option value="" disabled selected' + '>'+ "Selecciona Categoria" + '</option>';
Selector_Datos.innerHTML += '<option value="" disabled selected' + '>'+ "Cantidad de datos a ingresar" + '</option>';

//Funciones Adicionales
function ResizeSelect() {
  const selectElement = document.getElementById("Sel_Datos");
  const selectedOption = selectElement.options[selectElement.selectedIndex];
  const textWidth = selectedOption.text.length;
  selectElement.style.width = textWidth * 40 + "px"; // Ajusta el factor de multiplicación según tus necesidades
}

//Funciones ejecutadas cuando se detectan "Cambios"
Selector_Categoria.onchange = function () {
  Cate_Seleccionada = Selector_Categoria.value;
  
  fetch("/Cliente/HC_Calculada/SeleccionCategoria/" + Cate_Seleccionada).then(    
    function(Respuesta) {        
        Respuesta.json().then(function(Datos) {
          let optionHTML = '';
          for (let Fuente of Datos.Fuentes){
            optionHTML += '<option value="'+ Fuente + '">'+ Fuente +'</option>';
          }
          Selector_Fuente.innerHTML = optionHTML;
          Selector_Fuente.innerHTML += '<option value="" disabled selected' + '>'+ "Selecciona Fuente" + '</option>';

        });
      });    
}

Selector_Datos.onchange = function () 
{
  var Cantidad = parseInt(Selector_Datos.value);
  inputContainer.innerHTML = ""; // Limpiamos el contenedor antes de agregar los inputs

  for (var i = 1; i <= Cantidad; i++) {
    var input = document.createElement("input");
    input.type = "text";
    input.className = "form-control-sm";
    input.name = "txtDato_" + i;
    input.id = "txtDato_" + i;
    inputContainer.appendChild(input);
  }
}

//Asignación de funciones Adicionales
Selector_Datos.addEventListener("change", ResizeSelect);



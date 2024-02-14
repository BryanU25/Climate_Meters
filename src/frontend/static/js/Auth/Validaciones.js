// Función para validar la contraseña en tiempo real
function Validar_Password(password) {
  var regex = /^(?=.*[0-9])(?=.*[!@#$%^&*])(.{6,20})$/;
  var mensaje = "";

  if (password.length === 0) {
    mensaje = "La contraseña no puede estar vacía.";
  } else if (!regex.test(password)) {
    mensaje =
      "La contraseña debe tener al menos un número y un carácter especial y tener entre 6 y 20 caracteres.";
  }

  $("#password-error").text(mensaje);
}

// Función para validar el correo en tiempo real
function Validar_Email(email) {
  var regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  var mensaje = "";

  if (email.length === 0) {
    mensaje = "El campo email no puede estar vacío.";
  } else if (!regex.test(email)) {
    mensaje = "Ingrese una dirección de correo electrónico válida.";
  }

  $("#email-error").text(mensaje);
}

// Función para validar el usuario cumpla con los parametros
function Validar_User(user) {
    var regex = /^[a-zA-Z0-9]{4,30}$/;
    var mensaje = "";
  
    if (user.length === 0) {
      mensaje = "El usuario no puede estar vacío.";
    } else if (!regex.test(user)) {
      mensaje = "El usuario solo puede contener caracteres alfanuméricos.";
    }
  
    $("#user-error").text(mensaje);
  }

  // Función para validar la coincidencia de contraseñas
function Coincidencia_Password(contraseña1, contraseña2) {
  var mensaje = "";

  if (contraseña1 !== contraseña2) {
    mensaje = "Las contraseñas no coinciden.";
  }

  $("#confirmar-contraseña-error").text(mensaje);
}

// Validación Dinamica de los campos del formulario:

$(document).ready(function () {
  // Evento de escucha para el campo de contraseña
  $("#" + passwordId).on("input", function () {
      Validar_Password($(this).val());
  });

  // Evento de escucha para el campo de correo electrónico
  $("#" + emailId).on("input", function () {
      Validar_Email($(this).val());
  });

  // Evento de escucha para el campo de usuario
  $("#" + userId).on("input", function () {
      Validar_User($(this).val());
  });

  // Evento de escucha para el campo de Contraseña2
  $("#" + confirmId).on("input", function () {
      Coincidencia_Password($(this).val());
  });
});
  
//Obtención (Formulario)
function ObtenerDatos_Registro() {
  const Nombre = document.getElementById("Nombre").value;7
  const Apellido = document.getElementById("Apellido").value;
  const Correo = document.getElementById("Correo").value;
  const Usuario = document.getElementById("Usuario").value;
  const Password1 = document.getElementById("Password1").value;    
  const Password2 = document.getElementById("Password2").value;    
  return {
    Nombre: Nombre,
    Apellido: Apellido,
    Correo: Correo,
    Usuario: Usuario,
    Password1: Password1,
    Password2: Password2
  };
}

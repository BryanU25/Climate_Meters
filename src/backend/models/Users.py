from backend.database.db import db
from werkzeug.security import generate_password_hash, check_password_hash

class Users(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    Nombre = db.Column(db.String(40), nullable=False)
    Apellido = db.Column(db.String(40), nullable=False)
    Correo = db.Column(db.String(120), unique=True, nullable=False)
    Usuario = db.Column(db.String(80), unique=True, nullable=False)
    Password = db.Column(db.String(128), nullable=False)

    # Definir una clave foránea para la relación de roles
    Rol_idRol = db.Column(db.BigInteger, db.ForeignKey("roles.id"), nullable=False)

    # Establecer la relación "muchos a uno" con la tabla Roles
    rol = db.relationship("Roles", back_populates="user")

    def __init__(self, Nombre, Apellido, Correo, Usuario, Password, Rol_idRol):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Correo = Correo
        self.Usuario = Usuario
        self.Password = Password
        self.Rol_idRol = Rol_idRol

    @classmethod
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        return self.password_hash

    @classmethod
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

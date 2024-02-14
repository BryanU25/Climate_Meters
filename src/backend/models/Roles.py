from backend.database.db import db


class Roles(db.Model):
    __tablename__ = "roles"
    
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    Titulo = db.Column(db.String(50), unique=True, nullable=False)

    # Establecer la relación "muchos a uno" con la tabla User
    user = db.relationship("Users", back_populates="rol")

    def __init__(self, Titulo):
        self.Titulo = Titulo
    
    @classmethod
    def buscar_por_Titulo(self, titulo):
        return self.query.filter_by(Titulo=titulo).first()

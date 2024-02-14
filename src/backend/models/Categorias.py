from backend.database.db import db


class Categorias(db.Model):
    __tablename__ = "categorias"

    idCategorias = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    Nombre = db.Column(db.String(45), nullable=False)
    Descripcion = db.Column(db.Text)
    Unidad = db.Column(db.String(45), nullable=False)

    comb_solidos = db.relationship("CombustiblesSolidos", back_populates="catego")
    comb_liquidos = db.relationship("CombustiblesLiquidos", back_populates="catego")

    def __init__(self, Nombre, Descripcion, Unidad):
        self.Nombre = Nombre
        self.Descripcion = Descripcion
        self.Unidad = Unidad

    # Funcion para encontrar el nombre de la categoria
    @classmethod
    def buscar_por_nombre(self, nombre):
        return self.query.filter_by(Nombre=nombre).first()

from backend.database.db import db, ma

class HuellaGenerada(db.Model):
    __tablename__ = 'hc_calculadora'

    idHC_Generada = db.Column(db.Integer, primary_key=True, autoincrement=True)
    User_ID = db.Column(db.String(45), nullable=False)
    Fecha = db.Column(db.Date, nullable=False)
    Categoria = db.Column(db.String(45), nullable=False)
    Fuente = db.Column(db.String(45), nullable=False)
    Cantidad = db.Column(db.Float, nullable=False)
    Unidad = db.Column(db.String(45), nullable=False)
    Generado = db.Column(db.Float, nullable=False)

    def __init__(self, User_ID, Fecha, Categoria, Fuente, Cantidad, Unidad, Generado):
        self.User_ID = User_ID
        self.Fecha = Fecha
        self.Categoria = Categoria
        self.Fuente = Fuente
        self.Cantidad = Cantidad
        self.Unidad = Unidad
        self.Generado = Generado

# Clase Esquema
class HuellaGeneradaEsquema(ma.Schema):
    class Meta:
        fields = ('User_ID', 'Fecha', 'Categoria', 'Fuente', 'Cantidad', 'Unidad', 'Generado')
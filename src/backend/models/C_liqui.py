from backend.database.db import db, ma


class CombustiblesLiquidos(db.Model):
    __tablename__ = "combustibles_liquidos"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    Nombre = db.Column(db.String(45), unique=True, nullable=False)
    CO2 = db.Column(db.Float)
    CH4_F = db.Column(db.Float)
    N2O_F = db.Column(db.Float)
    CH4_M = db.Column(db.Float)
    N2O_M = db.Column(db.Float)

    # Definir una clave foránea para la relación
    Categorias_idCategorias = db.Column(
        db.BigInteger, db.ForeignKey("categorias.idCategorias")
    )

    # Establecer la relación "muchos a uno" con la tabla Categorias
    catego = db.relationship("Categorias", back_populates="comb_liquidos")

    def __init__(
        self, Nombre, CO2, CH4_F, N2O_F, CH4_M, N2O_M, Categorias_idCategorias
    ):
        self.Nombre = Nombre
        self.CO2 = CO2
        self.CH4_F = CH4_F
        self.N2O_F = N2O_F
        self.CH4_M = CH4_M
        self.N2O_M = N2O_M
        self.Categorias_idCategorias = Categorias_idCategorias

    # Funcion para encontrar la instancia a partir de la id
    @classmethod
    def buscar_por_id(self, id):
        return self.query.filter_by(id=id).first()

    @classmethod
    def buscar_por_nombre(self, nombre):
        return self.query.filter_by(Nombre=nombre).first()

    @classmethod
    def obtener_todo(self):
        instancias = self.query.all()
        return instancias

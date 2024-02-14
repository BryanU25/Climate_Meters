from backend.database.db import db, ma

# Modelo para la tabla catalogo_relaciones
class CatalogoRelaciones(db.Model):
    __tablename__ = 'catalogo_relaciones'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_categoria = db.Column(db.String(45))
    nombre_relacion = db.Column(db.String(45))
# Cuando agregues una nueva categoría o relación, inserta una fila en la tabla Categoria_Relaciones

    # Para acceder a las relaciones de una categoría específica:
    @classmethod
    def obtener_relacion_de_categoria(self, Nombre):
        relacion = self.query.filter_by(nombre_categoria=Nombre).first()
        return relacion.nombre_relacion

    @classmethod
    def obtener_todas_relaciones(self):
        relaciones = self.query.all()
        return relaciones

#Clase Esquema

class CatalogoRelacionesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre_categoria', 'nombre_relacion')

# Modelo para la tabla catalogo_categorias
class CatalogoCategorias(db.Model):
    __tablename__ = 'catalogo_categorias'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_categoria = db.Column(db.String(45), unique=True, nullable=False)
    clase_modelo = db.Column(db.String(45), nullable=False)



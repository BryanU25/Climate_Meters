from backend.database.db import ma
from backend.models.C_liqui import CombustiblesLiquidos
from backend.models.C_solid import CombustiblesSolidos
from marshmallow import validates, validates_schema, ValidationError

#Esquema de Compuestos (Instancias)
class InstanciaSchema(ma.Schema):
    class Meta:        
        fields = ('id', 'Nombre', 'CO2', 'CH4_F', 'N2O_F', 'CH4_M', 'N2O_M')
       
    @validates_schema
    def validate_fields(self, data, **kwargs):
        for field in ['CO2', 'CH4_F', 'N2O_F', 'CH4_M', 'N2O_M']:
            if field in data:
                try:
                    float_value = float(str(data[field]))
                    if float_value < 0:
                        raise ValidationError(f'El valor de {field} debe ser un número positivo.')
                except ValueError:
                    raise ValidationError(f'El valor de {field} debe ser un número válido.')

#Esquema de Usuarios (Registro)
class New_User(ma.Schema):
    class Meta:
        fields = ('id', 'Nombre', 'Apellido', 'Correo', 'Usuario', 'Password')
        
# Función para generar esquemas dinámicamente
def generar_esquemas(modelo):
    class Esquema(ma.SQLAlchemyAutoSchema):
        class Meta:
            model = modelo
            load_instance = True  # Cargar instancias del modelo durante la deserialización

    return Esquema

# Generar esquemas para tus modelos
CombustibleSolidoSchema = generar_esquemas(CombustiblesSolidos)
CombustibleLiquidoSchema = generar_esquemas(CombustiblesLiquidos)

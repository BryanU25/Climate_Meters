from flask import Flask
from backend.database.config import get_connection
from backend.database.db import init_db
from flask_wtf.csrf import CSRFProtect

# Rutas
from backend.routes.admin.HC_admins import HC_admins
from backend.routes.client.Huella_Carbono import HuellaCarbono

app = Flask(__name__)

# Configuraciones
Conexion = get_connection()
app.template_folder = "../frontend/templates"
app.static_folder = "../frontend/static"
app.config["SQLALCHEMY_DATABASE_URI"] = Conexion
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = '\x83`HS\tU\xc7\x19\xfcKJ\xe9\xc6\x0b0\x8c\xea\x1fJ\x07\x83\xd7>x'

csrf = CSRFProtect(app)

# Blueprints
app.register_blueprint(HC_admins)
app.register_blueprint(HuellaCarbono)


init_db(app)
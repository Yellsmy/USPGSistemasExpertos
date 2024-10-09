from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('../config.py')

    # Inicialización de la base de datos
    db.init_app(app)

    # Habilitación de CORS para todas las rutas
    CORS(app)

    # Registro de Blueprints
    from .Routes import recomendaciones
    app.register_blueprint(recomendaciones.bp)

    # Registrar el blueprint para servir las imágenes
    from .Routes import uploads
    app.register_blueprint(uploads.bp_uploads)

    return app


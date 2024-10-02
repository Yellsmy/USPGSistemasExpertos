from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('../config.py')

    db.init_app(app)

    from .Routes import recomendaciones
    app.register_blueprint(recomendaciones.bp)

    return app

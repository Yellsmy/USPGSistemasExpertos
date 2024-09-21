from flask import Blueprint
from .recomendaciones import bp as recomendaciones_bp

def init_app(app):
    app.register_blueprint(recomendaciones_bp)

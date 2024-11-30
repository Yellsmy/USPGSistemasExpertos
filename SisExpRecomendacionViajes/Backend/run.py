from App import create_app
import os
from App.Routes.auth import auth_bp
from App.Routes.protected import protected_bp
from App.Routes.personalized import personalized_bp

# Crear la aplicación Flask
app = create_app()

# Configuración para servir la carpeta 'uploads' como estática
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')

# Registrar blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')  # Rutas de autenticación
app.register_blueprint(protected_bp, url_prefix='/protected')  # Rutas protegidas
app.register_blueprint(personalized_bp, url_prefix='/recommendations')  # Rutas para recomendaciones personalizadas

if __name__ == "__main__":
    # Iniciar la aplicación Flask
    app.run(debug=True)




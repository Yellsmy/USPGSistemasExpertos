from App import create_app
import os

app = create_app()

# Configuración para servir la carpeta 'uploads' como estática
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')

if __name__ == "__main__":
    app.run(debug=True)

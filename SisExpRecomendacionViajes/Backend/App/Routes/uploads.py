from flask import Blueprint, send_from_directory, jsonify, current_app
import os

bp_uploads = Blueprint('uploads', __name__)

# Ruta para servir las imágenes desde la carpeta uploads
@bp_uploads.route('/uploads/<filename>')
def uploaded_file(filename):
    try:
        # Obtener la ruta completa de la carpeta 'uploads'
        uploads_dir = os.path.join(current_app.root_path, 'uploads')
        #print(f"Buscando imagen en: {uploads_dir}")
        return send_from_directory(uploads_dir, filename)
    except Exception as e:
        return jsonify({"mensaje": f"Error al obtener la imagen: {str(e)}"}), 404

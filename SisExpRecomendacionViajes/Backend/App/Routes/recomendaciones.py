from flask import Blueprint, request, jsonify
from App.Services.agregar_recomendacion import agregar_recomendacion
from App.Services.obtener_recomendaciones import inferir_recomendaciones
from datetime import datetime
import os
from flask import current_app
from werkzeug.utils import secure_filename

bp = Blueprint('recomendaciones', __name__)

# Ruta para agregar recomendaciones
@bp.route('/recomendaciones', methods=['POST'])
def agregar_recomendacion_route():
    try:
        data = {
            "destino": request.form['destino'],
            "actividad": request.form['actividad'],
            "epoca": request.form['epoca'],
            "presupuesto": request.form['presupuesto'],
            "latitud": float(request.form['latitud']),
            "longitud": float(request.form['longitud']),
            "pais": request.form['pais']
        }
        if 'imagen' not in request.files:
            return jsonify({"mensaje": "Falta el archivo de imagen"}), 400

        # Obtener la imagen del formulario
        imagen = request.files['imagen']

        # Nombre del archivo sea seguro
        filename = secure_filename(imagen.filename)

        # Definición la ruta hacia la carpeta uploads donde se almacenará la imagen
        upload_folder = current_app.config['UPLOAD_FOLDER']
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)

        # Guarda la imagen en la carpeta uploads
        image_path = os.path.join(upload_folder, filename)
        imagen.save(image_path)

        # Crear la URL completa para la imagen
        image_url = f'/uploads/{filename}'
        data['imagen'] = image_url

        # Agregar la recomendación 
        mensaje, status_code = agregar_recomendacion(data)
        return jsonify(mensaje), status_code

    except Exception as e:
        #print(f"Error al agregar la recomendación: {str(e)}")
        return jsonify({"mensaje": f"Error: {str(e)}"}), 500

# Ruta para obtener las recomendaciones
@bp.route('/recomendaciones/buscar', methods=['POST'])
def obtener_recomendaciones_route():
    try:
        data = request.get_json()
        preferencia = data['preferencia']
        temporada = data['temporada']
        presupuesto = data['presupuesto']
        latitud_usuario = float(data['latitud'])
        longitud_usuario = float(data['longitud'])
        pais = data['pais']
        fecha_viaje = datetime.strptime(data['fecha_viaje'], '%Y-%m-%d')

        destinos = inferir_recomendaciones(preferencia, temporada, presupuesto, latitud_usuario, longitud_usuario, pais, fecha_viaje)

        if destinos:
            return jsonify({"recomendaciones": destinos}), 200
        else:
            return jsonify({"mensaje": "No hay recomendaciones disponibles"}), 404

    except Exception as e:
        return jsonify({"mensaje": f"Error: {str(e)}"}), 500


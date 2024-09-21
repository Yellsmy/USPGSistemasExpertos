from datetime import datetime
from flask import Blueprint, request, jsonify
from App.Services.agregar_recomendacion import agregar_recomendacion
from App.Services.obtener_recomendaciones import inferir_recomendaciones
from flask import Blueprint, request, jsonify

bp = Blueprint('recomendaciones', __name__)

# Ruta para la página principal
@bp.route('/')
def index():
    return "Bienvenido a la API de recomendaciones de viajes"

# Ruta para agregar una nueva recomendación
@bp.route('/recomendaciones', methods=['POST'])
def agregar_recomendacion_route():
    print("Solicitud POST recibida en /recomendaciones")
    data = request.get_json()
    mensaje, status_code = agregar_recomendacion(data)
    return jsonify(mensaje), status_code


# Ruta para obtener recomendaciones
@bp.route('/recomendaciones/buscar', methods=['POST'])
def obtener_recomendaciones_route():
    data = request.get_json()

    preferencia = data['preferencia']
    temporada = data['temporada']
    presupuesto = data['presupuesto']
    latitud_usuario = data['latitud']
    longitud_usuario = data['longitud']
    pais_id = data['pais_id']
    region_id = data.get('region_id') 
    fecha_viaje = datetime.strptime(data['fecha_viaje'], '%Y-%m-%d')

    destinos = inferir_recomendaciones(preferencia, temporada, presupuesto, latitud_usuario, longitud_usuario, pais_id, region_id, fecha_viaje)

    if destinos:
        return jsonify({"recomendaciones": destinos})
    else:
        return jsonify({"mensaje": "No hay recomendaciones disponibles"}), 404

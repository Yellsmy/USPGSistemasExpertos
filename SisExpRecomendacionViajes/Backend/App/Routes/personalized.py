from flask import Blueprint, request, jsonify
from App.Services.personalized_recommendation import PersonalizedRecommendationService

personalized_bp = Blueprint('personalized_recommendations', __name__)

from flask import Blueprint, request, jsonify
from App.Services.personalized_recommendation import PersonalizedRecommendationService
from flask import current_app
import jwt
from App.Models.UserRecommendationHistory import UserRecommendationHistory
from App import db
# Crear el Blueprint para las rutas personalizadas
personalized_bp = Blueprint('personalized_recommendations', __name__)

@personalized_bp.route('/personalized', methods=['POST'])
def personalized_recommendations():
    try:
        # Obtener los datos del cuerpo de la solicitud
        data = request.get_json()
        preferencia = data.get('preferencia')
        presupuesto = data.get('presupuesto')
        latitud_usuario = data.get('latitud')
        longitud_usuario = data.get('longitud')
        paisIngreso = data.get('pais')
        fecha_viaje = data.get('fecha_viaje')
        people_count = data.get('people_count')

        # Validar campos obligatorios
        if not all([preferencia, presupuesto, latitud_usuario, longitud_usuario, paisIngreso, fecha_viaje, people_count]):
            return jsonify({"message": "Todos los campos son obligatorios"}), 400

        # Convertir fecha_viaje a datetime
        from datetime import datetime
        try:
            fecha_viaje = datetime.strptime(fecha_viaje, '%Y-%m-%d')
        except ValueError:
            return jsonify({"message": "Formato de fecha inválido. Use 'YYYY-MM-DD'."}), 400

        # Obtener las recomendaciones personalizadas
        recomendaciones = PersonalizedRecommendationService.get_personalized_recommendations(
            preferencia=preferencia,
            presupuesto=presupuesto,
            latitud_usuario=float(latitud_usuario),
            longitud_usuario=float(longitud_usuario),
            paisIngreso=paisIngreso,
            fecha_viaje=fecha_viaje,
            people_count=int(people_count)
        )

        # Retornar las recomendaciones
        return jsonify({"recomendaciones": recomendaciones}), 200

    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500



@personalized_bp.route('/personalized/user-recommendations', methods=['GET'])
def user_recommendations():
    """
    Ruta para obtener recomendaciones basadas en el historial del usuario.
    """
    try:
        # Obtener el token del encabezado Authorization
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({"message": "Token faltante"}), 401

        # Validar formato del token
        if not auth_header.startswith("Bearer "):
            return jsonify({"message": "Formato de token inválido"}), 401
        token = auth_header.split(" ")[1]

        # Decodificar el token
        try:
            decoded = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            user_id = decoded.get('user_id')
            if not user_id:
                raise ValueError("Usuario no identificado en el token")
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Token inválido"}), 401

        # Llamar al servicio para obtener las recomendaciones basadas en el historial
        recomendaciones = PersonalizedRecommendationService.get_user_based_recommendations(user_id)

        # Retornar las recomendaciones en formato JSON
        return jsonify({"recomendaciones": recomendaciones}), 200

    except Exception as e:
        # Manejar errores y retornar el mensaje
        return jsonify({"message": f"Error: {str(e)}"}), 500


@personalized_bp.route('/personalized/select', methods=['POST'])
def select_recommendation():
    """
    Guarda una recomendación seleccionada por el usuario en el historial.
    """
    try:
        # Obtener el token del encabezado Authorization
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({"message": "Token faltante"}), 401

        # Validar formato del token
        if not auth_header.startswith("Bearer "):
            return jsonify({"message": "Formato de token inválido"}), 401
        token = auth_header.split(" ")[1]

        # Decodificar el token
        try:
            decoded = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            user_id = decoded.get('user_id')
            if not user_id:
                raise ValueError("Usuario no identificado en el token")
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Token inválido"}), 401

        # Obtener datos del cuerpo de la solicitud
        data = request.get_json()
        recommendation_id = data.get('recommendation_id')

        if not recommendation_id:
            return jsonify({"message": "El ID de la recomendación es obligatorio"}), 400

        # Insertar en el historial
        new_entry = UserRecommendationHistory(
            user_id=user_id,
            recommendation_id=recommendation_id
        )
        db.session.add(new_entry)
        db.session.commit()

        return jsonify({"message": "Recomendación guardada en el historial"}), 201

    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500

@personalized_bp.route('/personalized/destination/<int:destination_id>', methods=['GET'])
def get_destination(destination_id):
    """
    Endpoint para obtener los detalles de un destino específico por ID.
    """
    try:
        # Obtener detalles del destino
        destination_details = PersonalizedRecommendationService.get_destination_details(destination_id)
        return jsonify({"destino": destination_details}), 200
    except ValueError as ve:
        return jsonify({"message": str(ve)}), 404
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500

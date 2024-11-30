from App.Models.recomendaciones import Recomendacion
from App.Models.pronostico import Pais
from App.Services.climate_prediction import ClimatePredictionService
from flask import current_app
from datetime import datetime  # Importar datetime para validaciones

from App.Models.activities import Activity
from App.Models.accommodation import Accommodation
from App.Models.restaurants import Restaurant
from App.Models.climate_history import ClimateHistory
from App.Services.climate_prediction import ClimatePredictionService
from App.Models.recomendaciones import Recomendacion
from App.Models.pronostico import Pais
from App.Models.UserRecommendationHistory import UserRecommendationHistory
from App import db
from sqlalchemy import text
from App.ML.recommendation_model import UserRecommendationModel

class PersonalizedRecommendationService:
    @staticmethod
    def get_personalized_recommendations(preferencia, presupuesto, latitud_usuario, longitud_usuario, paisIngreso, fecha_viaje, people_count):
        # Verificar el país
        print("PAIS", paisIngreso)
        pais = Pais.query.filter_by(pais=paisIngreso).first()
        if not pais:
            raise ValueError("País no encontrado")

        pais_id = pais.id_pais

        # Filtrar recomendaciones según presupuesto
        if presupuesto == "Alto":
            recomendaciones = Recomendacion.query.filter(
                Recomendacion.actividad == preferencia,
                Recomendacion.id_pais != pais_id
            ).all()
        elif presupuesto == "Medio":
            recomendaciones = Recomendacion.query.filter(
                Recomendacion.actividad == preferencia,
                Recomendacion.id_pais == pais_id
            ).all()
        elif presupuesto == "Bajo":
            recomendaciones = Recomendacion.query.filter(
                Recomendacion.actividad == preferencia,
                Recomendacion.id_pais == pais_id
            ).all()
        else:
            raise ValueError("Presupuesto no válido")

        destinos = []
        for recomendacion in recomendaciones:
            # Predecir clima con el nuevo modelo
            prediction = ClimatePredictionService.predict(paisIngreso, fecha_viaje)

            # Generar itinerario para el destino
            itinerary = PersonalizedRecommendationService.generate_itinerary(recomendacion.destino, presupuesto, people_count)

            # Preparar la respuesta
            destinos.append({
                "id": recomendacion.id,  # Asegurarse de incluir el ID
                "destino": recomendacion.destino,
                "clima": prediction["clima"],
                "temperatura_minima": prediction["temperatura_minima"],
                "temperatura_maxima": prediction["temperatura_maxima"],
                "temporada": prediction["temporada"],
                "imagen_url": recomendacion.imagen,
                "itinerario": itinerary
            })

        return destinos

    @staticmethod
    def generate_itinerary(destination, presupuesto, people_count):
        # Obtener actividades
        activities = Activity.query.filter_by(destination=destination).all()
        selected_activities = [{"name": a.name, "price": a.price, "duration": a.duration_hours} for a in activities]

        # Obtener alojamiento
        accommodation = Accommodation.query.filter_by(destination=destination).first()
        selected_accommodation = {
            "type": accommodation.type,
            "price_per_night": accommodation.price_per_night
        } if accommodation else {}

        # Obtener comida
        restaurants = Restaurant.query.filter_by(destination=destination).all()
        selected_restaurants = [{"name": r.name, "price_per_person": r.price_per_person} for r in restaurants]

        # Calcular costos
        activities_cost = sum([a["price"] for a in selected_activities])
        accommodation_cost = selected_accommodation.get("price_per_night", 0) * people_count  # Asume 1 noche
        food_cost = sum([r["price_per_person"] * people_count for r in selected_restaurants])

        total_cost = activities_cost + accommodation_cost + food_cost

        return {
            "actividades": selected_activities,
            "alojamiento": selected_accommodation,
            "comida": selected_restaurants,
            "costo_total": total_cost
        }


    from sqlalchemy import text

    @staticmethod
    def get_user_based_recommendations(user_id):
        """
        Obtiene recomendaciones basadas en el historial del usuario.
        """
        try:
            # Definir la consulta SQL
            query = text("""
                SELECT r.id AS id, r.destino AS destino, r.actividad AS actividad, 
                    r.presupuesto AS presupuesto, r.imagen AS imagen
                FROM user_recommendations_history h
                JOIN recomendacion r ON h.recommendation_id = r.id
                WHERE h.user_id = :user_id
            """)

            # Ejecutar la consulta con el parámetro seguro
            results = db.session.execute(query, {"user_id": user_id}).fetchall()

            # Convertir los resultados a una lista de diccionarios manualmente
            recomendaciones = [
                {
                    "id": row[0],
                    "destino": row[1],
                    "actividad": row[2],
                    "presupuesto": row[3],
                    "imagen_url": row[4]
                }
                for row in results
            ]

            return recomendaciones
        except Exception as e:
            raise ValueError(f"Error al obtener recomendaciones: {str(e)}")




    @staticmethod
    def get_destination_details(destination_id):
        # Buscar el destino en la tabla Recomendaciones
        recomendacion = Recomendacion.query.get(destination_id)
        if not recomendacion:
            raise ValueError("Destino no encontrado")

        # Generar el itinerario del destino
        itinerary = PersonalizedRecommendationService.generate_itinerary(
            destination=recomendacion.destino,
            presupuesto=recomendacion.presupuesto,
            people_count=1  # Default hasta que el usuario indique más adelante
        )

        # Preparar los datos del destino
        return {
            "destino": recomendacion.destino,
            "actividad": recomendacion.actividad,
            "presupuesto": recomendacion.presupuesto,
            "imagen_url": recomendacion.imagen,
            "itinerario": itinerary
        }


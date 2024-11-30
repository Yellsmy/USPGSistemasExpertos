'''from App.ML.predict import predict_climate
from App.Models.climate_history import ClimateHistory

class ClimatePredictionService:
    @staticmethod
    def predict(country, fecha_viaje):
        try:
            # Consulta para obtener los datos del clima
            climate_data = ClimateHistory.query.filter_by(
                country=country, date=fecha_viaje
            ).first()

            if not climate_data:
                raise ValueError(f"No hay datos climáticos disponibles para {country} en {fecha_viaje}.")

            # Determina el clima según la precipitación
            clima = "Soleado" if climate_data.precipitation < 0.1 else "Lluvioso"

            # Retorna el clima y otros detalles
            return {
                "clima": clima,
                "temperatura_minima": climate_data.temperature_min,
                "temperatura_maxima": climate_data.temperature_max,
                "temporada": climate_data.season,
            }
        except Exception as e:
            raise ValueError(f"Error al predecir el clima: {str(e)}")
'''

from App.ML.predict import predict_climate

class ClimatePredictionService:
    @staticmethod
    def predict(country, fecha_viaje):
        try:
            # Extraer el mes de la fecha de viaje
            month = fecha_viaje.month

            # Usar el modelo para predecir
            climate_data = predict_climate(month)

            # Determinar la temporada (puedes ajustarlo según tu lógica)
            temporada = ClimatePredictionService.get_season(month)
            climate_data["temporada"] = temporada

            return climate_data
        except Exception as e:
            raise ValueError(f"Error al predecir el clima: {str(e)}")

    @staticmethod
    def get_season(month):
        if month in [5, 6, 7, 8, 9, 10]:
            return "Invierno"  # Temporada de lluvias
        elif month in [11, 12, 1, 2, 3, 4]:
            return "Verano"  # Temporada seca
        else:
            return "Desconocido"



from joblib import load
import os

# Ruta correcta según tu estructura
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
model_min_path = os.path.join(base_path, "ML/temp_min_model.joblib")
model_max_path = os.path.join(base_path, "ML/temp_max_model.joblib")

# Cargar los modelos entrenados
try:
    model_min = load(model_min_path)
    model_max = load(model_max_path)
    print(f"Modelos cargados correctamente desde:\n{model_min_path}\n{model_max_path}")
except FileNotFoundError as e:
    raise FileNotFoundError(f"Error cargando modelos: {str(e)}")

def predict_climate(month):
    try:
        # Convertir mes en array para el modelo
        month_array = [[month]]

        # Realizar predicciones
        temp_min = model_min.predict(month_array)[0]
        temp_max = model_max.predict(month_array)[0]

        # Retornar resultados
        return {
            "clima": "Soleado" if temp_max > 25 else "Lluvioso",
            "temperatura_minima": round(temp_min, 2),
            "temperatura_maxima": round(temp_max, 2)
        }
    except Exception as e:
        raise ValueError(f"Error en la predicción del clima: {str(e)}")

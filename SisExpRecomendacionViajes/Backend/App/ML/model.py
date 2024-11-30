import sys
import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from joblib import dump

# Agregar la ruta absoluta directamente al sistema de búsqueda
sys.path.append("C:/Users/Usuario/Desktop/USPG/SISTEMAS EXPERTOS/USPGSistemasExpertos/SisExpRecomendacionViajes/Backend")

# Importar la aplicación Flask y la base de datos
from App import create_app, db
from App.Models.climate_data import ClimateData

# Crear la aplicación para configurar el contexto
app = create_app()

with app.app_context():  # Configurar el contexto de la aplicación
    try:
        # Consulta para obtener los datos del clima desde la tabla climate_data
        query = "SELECT month, temperature_min, temperature_max FROM climate_data"

        # Cargar los datos desde la base de datos
        data = pd.read_sql(query, con=db.engine)

        # Verificar que los datos se cargaron correctamente
        if data.empty:
            print("La tabla 'climate_data' no tiene datos.")
            sys.exit()

        # Separar los datos en variables independientes (X) y dependientes (y)
        X = data[['month']]  # Mes del año como variable independiente
        y_min = data['temperature_min']  # Temperatura mínima como variable dependiente
        y_max = data['temperature_max']  # Temperatura máxima como variable dependiente

        # Dividir los datos en conjuntos de entrenamiento y prueba
        X_train, X_test, y_min_train, y_min_test = train_test_split(X, y_min, test_size=0.2, random_state=42)
        X_train, X_test, y_max_train, y_max_test = train_test_split(X, y_max, test_size=0.2, random_state=42)

        # Crear y entrenar los modelos de regresión lineal
        model_min = LinearRegression()
        model_max = LinearRegression()

        model_min.fit(X_train, y_min_train)
        model_max.fit(X_train, y_max_train)

        # Guardar los modelos entrenados en archivos
        os.makedirs("App/ML", exist_ok=True)  # Crear la carpeta ML si no existe
        dump(model_min, 'App/ML/temp_min_model.joblib')
        dump(model_max, 'App/ML/temp_max_model.joblib')

        print("Modelos entrenados y guardados exitosamente.")
    except Exception as e:
        print(f"Error al entrenar y guardar los modelos: {str(e)}")

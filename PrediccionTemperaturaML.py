import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Datos de temperatura simulados
data = {
    'Año': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 
            2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
    'Temperatura': [14.1, 14.2, 14.3, 14.5, 14.4, 14.6, 14.8, 14.7, 14.6, 
                    14.9, 15.0, 15.1, 15.3, 15.2, 15.5, 15.6, 15.8, 15.7, 
                    15.9, 16.0]
}
df = pd.DataFrame(data)

# Preparar los datos para el modelo
X = df[['Año']]
y = df['Temperatura']

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Hacer las predicciones
y_pred = modelo.predict(X_test)

# Visualizar la tendencia de temperatura y el modelo
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Datos reales')
plt.plot(X, modelo.predict(X), color='red', label='Tendencia lineal (predicción)')
plt.xlabel('Año')
plt.ylabel('Temperatura promedio (°C)')
plt.title('Análisis de tendencias de temperatura')
plt.legend()
plt.show()

# Calcular la pendiente y la intersección de la recta
print(f"Pendiente (cambio por año): {modelo.coef_[0]:.4f}")
print(f"Intersección (temperatura inicial): {modelo.intercept_:.4f}")

# Calcular el puntaje de precisión del modelo (opcional)
puntaje = modelo.score(X_test, y_test)
print(f"Precisión del modelo (R^2): {puntaje:.4f}")

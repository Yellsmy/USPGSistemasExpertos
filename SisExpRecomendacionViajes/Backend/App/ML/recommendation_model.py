import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sqlalchemy.sql import text  # Importar text para consultas SQL
from App import db

class UserRecommendationModel:
    @staticmethod
    def train_and_predict(user_id):
        # Consulta SQL explícitamente declarada como texto
        query = text("""
            SELECT r.id AS recommendation_id, r.destino, r.actividad, r.presupuesto
            FROM user_recommendations_history h
            JOIN recomendacion r ON h.recommendation_id = r.id
            WHERE h.user_id = :user_id
        """)
        try:
            # Ejecutar la consulta usando db.session
            result = db.session.execute(query, {"user_id": user_id})
            data = pd.DataFrame(result.fetchall(), columns=["recommendation_id", "destino", "actividad", "presupuesto"])

            # Verificar si el usuario tiene suficiente historial
            if data.empty:
                raise ValueError("No hay historial suficiente para generar recomendaciones.")

            # Crear variables categóricas como datos de entrada
            features = pd.get_dummies(data[["actividad", "presupuesto"]])
            recommendation_ids = data["recommendation_id"]

            # Entrenar el modelo KNN con el historial del usuario
            knn = NearestNeighbors(n_neighbors=3, algorithm="auto")
            knn.fit(features)

            # Usar los mismos datos del usuario para predecir recomendaciones
            distances, indices = knn.kneighbors(features)
            recommended_indices = indices[0]  # Seleccionar índices de recomendaciones cercanas

            # Seleccionar las recomendaciones basadas en los índices
            recommendations = data.iloc[recommended_indices]

            # Formatear el resultado
            return [
                {
                    "destino": row["destino"],
                    "actividad": row["actividad"],
                    "presupuesto": row["presupuesto"]
                }
                for _, row in recommendations.iterrows()
            ]

        except Exception as e:
            raise ValueError(f"Error al entrenar y predecir: {str(e)}")

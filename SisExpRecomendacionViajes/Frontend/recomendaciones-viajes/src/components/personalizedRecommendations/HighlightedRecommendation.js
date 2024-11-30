import React, { useEffect, useState } from 'react';
import { obtenerHistorialRecomendaciones } from '../../services/recommendationsService';
import './HighlightedRecommendation.css';

const HighlightedRecommendation = () => {
  const [recommendation, setRecommendation] = useState(null);
  const [message, setMessage] = useState('');

  useEffect(() => {
    const fetchRecommendations = async () => {
      try {
        const data = await obtenerHistorialRecomendaciones();
        if (data.recomendaciones.length > 0) {
          setRecommendation(data.recomendaciones[0]); // Mostramos la primera recomendación
        } else {
          setMessage('Bienvenido, aquí se mostrarán las recomendaciones basadas en tu historial.');
        }
      } catch (error) {
        console.error('Error al obtener recomendaciones:', error);
        setMessage('No se pudieron cargar las recomendaciones. Por favor, intenta más tarde.');
      }
    };

    fetchRecommendations();
  }, []);

  if (message) {
    return <div className="welcome-message">{message}</div>;
  }

  return (
    <div className="highlighted-recommendation">
      <h2>Creemos que te podría gustar</h2>
      {recommendation && (
        <div className="recommendation-card">
          <img src={`http://127.0.0.1:5000${recommendation.imagen_url}`} alt={recommendation.destino} />
          <h3>{recommendation.destino}</h3>
          <p>Presupuesto: {recommendation.presupuesto}</p>
          <p>Actividad: {recommendation.actividad}</p>
          <button onClick={() => window.scrollTo({ top: 600, behavior: 'smooth' })}>
            Me interesa
          </button>
        </div>
      )}
    </div>
  );
};

export default HighlightedRecommendation;

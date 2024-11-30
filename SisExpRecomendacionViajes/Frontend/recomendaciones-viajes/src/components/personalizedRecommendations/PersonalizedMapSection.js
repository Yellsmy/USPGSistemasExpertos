import React, { useState, useEffect } from 'react';
import PersonalizedMap from './PersonalizedMap';
import {
  obtenerRecomendacionDestacada,
  seleccionarRecomendacion,
  buscarRecomendacionEspecifica,
} from '../../services/recomendacionesPersonalizadasService';
import './PersonalizedMapSection.css';

const PersonalizedMapSection = ({ setLatitud, setLongitud, setPais, setItinerario }) => {
  const [recomendaciones, setRecomendaciones] = useState([]);
  const [currentRecommendationIndex, setCurrentRecommendationIndex] = useState(0);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const fetchRecomendaciones = async () => {
      try {
        const recomendacionesObtenidas = await obtenerRecomendacionDestacada();
        if (recomendacionesObtenidas.length > 0) {
          setRecomendaciones(recomendacionesObtenidas);
        } else {
          setError('No hay recomendaciones disponibles.');
        }
      } catch (err) {
        setError(err.message);
      }
    };

    fetchRecomendaciones();
  }, []);

  const manejarSeleccion = async () => {
    const recomendacionActual = recomendaciones[currentRecommendationIndex];
    if (!recomendacionActual) return;

    try {
      setLoading(true);

      // Registra el interés en el destino
      await seleccionarRecomendacion(recomendacionActual.id);

      // Obtiene detalles completos del destino
      const detalles = await buscarRecomendacionEspecifica(recomendacionActual.id);
      console.log('Detalles obtenidos:', detalles); // Consola para verificar datos

      if (detalles?.destino?.itinerario) {
        setItinerario(detalles.destino.itinerario); // Actualiza el itinerario
      } else {
        throw new Error('Itinerario no disponible para este destino.');
      }

      // Desplaza al usuario a la sección de itinerario
      document.getElementById('section-itinerary').scrollIntoView({ behavior: 'smooth' });
    } catch (error) {
      setError(error.message || 'Error al procesar la recomendación.');
    } finally {
      setLoading(false);
    }
  };

  const siguienteRecomendacion = () => {
    setCurrentRecommendationIndex((prevIndex) => (prevIndex + 1) % recomendaciones.length);
  };

  const recomendacionActual = recomendaciones[currentRecommendationIndex];

  return (
    <div className="prueba-group">
      {/* Sección Destacada */}
      <div className="section-2">
        <h2>Creemos que te podría gustar</h2>
        {error ? (
          <p className="error-message">{error}</p>
        ) : recomendacionActual ? (
          <div className="featured-recommendation" onClick={siguienteRecomendacion}>
            <img
              src={`http://127.0.0.1:5000${recomendacionActual.imagen_url}`}
              alt={recomendacionActual.destino}
            />
            <div className="recommendation-info">
              <h3>{recomendacionActual.destino}</h3>
              <p>Clima: {recomendacionActual.clima}</p>
              <p>Presupuesto: {recomendacionActual.presupuesto}</p>
              <p>Temporada: {recomendacionActual.temporada}</p>
            </div>
            <button onClick={manejarSeleccion} disabled={loading}>
              {loading ? 'Cargando...' : 'Me interesa'}
            </button>
            <div className="navigation-arrow">
              <span>&#8594;</span>
            </div>
          </div>
        ) : (
          <p>Cargando recomendación...</p>
        )}
      </div>

      {/* Sección Mapa */}
      <div className="section-3-1 map-section">
        <h3>Selecciona tu ubicación en el mapa</h3>
        <PersonalizedMap setLatitud={setLatitud} setLongitud={setLongitud} setPais={setPais} />
      </div>
    </div>
  );
};

export default PersonalizedMapSection;

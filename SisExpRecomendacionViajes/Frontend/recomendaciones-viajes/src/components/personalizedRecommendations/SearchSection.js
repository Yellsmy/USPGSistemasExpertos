import React, { useState } from 'react';
import './SearchSection.css';
import {
  buscarRecomendacionesPersonalizadas,
  seleccionarRecomendacion,
  buscarRecomendacionEspecifica,
} from '../../services/recomendacionesPersonalizadasService';

const SearchSection = ({ latitud, longitud, pais, setItinerario }) => {
  const [preferencia, setPreferencia] = useState('');
  const [presupuesto, setPresupuesto] = useState('');
  const [fechaViaje, setFechaViaje] = useState('');
  const [cantidadPersonas, setCantidadPersonas] = useState(1);
  const [recomendaciones, setRecomendaciones] = useState([]);
  const [currentRecommendationIndex, setCurrentRecommendationIndex] = useState(0);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const buscarRecomendaciones = async () => {
    if (!latitud || !longitud || !pais) {
      setError('Por favor, selecciona tu ubicación en el mapa antes de buscar.');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const resultados = await buscarRecomendacionesPersonalizadas({
        preferencia,
        presupuesto,
        latitud,
        longitud,
        pais,
        fecha_viaje: fechaViaje,
        people_count: cantidadPersonas,
      });
      setRecomendaciones(resultados);
      setCurrentRecommendationIndex(0); // Reinicia al primer resultado
    } catch (err) {
      setError(err.message || 'Error al buscar recomendaciones.');
    } finally {
      setLoading(false);
    }
  };

  const manejarSeleccion = async () => {
    const recomendacionActual = recomendaciones[currentRecommendationIndex];
    if (!recomendacionActual) return;

    try {
      setLoading(true);

      // Guardar en historial
      await seleccionarRecomendacion(recomendacionActual.id);

      // Obtener detalles completos del destino
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

  const recomendacionActual =
    recomendaciones.length > 0 ? recomendaciones[currentRecommendationIndex] : null;

  return (
    <div className="search-section">
      {/* Sección 3.2: Criterios de búsqueda */}
      <div className="criteria-section">
        <h3>Personaliza tu búsqueda</h3>
        <select value={preferencia} onChange={(e) => setPreferencia(e.target.value)}>
          <option value="">Preferencia</option>
          <option value="Cultura">Cultura</option>
          <option value="Playa">Playa</option>
          <option value="Escalada">Escalada</option>
          <option value="Naturaleza">Naturaleza</option>
        </select>
        <select value={presupuesto} onChange={(e) => setPresupuesto(e.target.value)}>
          <option value="">Presupuesto</option>
          <option value="Bajo">Bajo</option>
          <option value="Medio">Medio</option>
          <option value="Alto">Alto</option>
        </select>
        <input
          type="date"
          value={fechaViaje}
          onChange={(e) => setFechaViaje(e.target.value)}
        />
        <input
          type="number"
          min="1"
          placeholder="Cantidad de personas"
          value={cantidadPersonas}
          onChange={(e) => setCantidadPersonas(e.target.value)}
        />
        <button onClick={buscarRecomendaciones}>Buscar</button>
        {loading && <p>Cargando recomendaciones...</p>}
        {error && <p className="error-message">{error}</p>}
      </div>

      {/* Sección 3.3: Tarjetas de recomendaciones */}
      <div className="recommendations-section">
        {recomendaciones.length === 0 ? (
          <p>No hay recomendaciones disponibles. Realiza una búsqueda para obtener resultados.</p>
        ) : (
          <div className="recommendation-card">
            <h3>Recomendaciones</h3>
            {recomendacionActual && (
              <>
                <img
                  src={`http://127.0.0.1:5000${recomendacionActual.imagen_url}`}
                  alt={recomendacionActual.destino}
                />
                <h4>{recomendacionActual.destino}</h4>
                <p>Clima: {recomendacionActual.clima}</p>
                <p>Presupuesto: {recomendacionActual.presupuesto}</p>
                <p>Temporada: {recomendacionActual.temporada}</p>
                <p>
                  Temperatura: {recomendacionActual.temperatura_minima}°C -{' '}
                  {recomendacionActual.temperatura_maxima}°C
                </p>
                <button onClick={manejarSeleccion} disabled={loading}>
                  {loading ? 'Cargando...' : 'Me interesa'}
                </button>
                <div className="navigation-buttons">
                  <button
                    onClick={() =>
                      setCurrentRecommendationIndex(
                        (prev) => (prev - 1 + recomendaciones.length) % recomendaciones.length
                      )
                    }
                  >
                    ←
                  </button>
                  <button
                    onClick={() =>
                      setCurrentRecommendationIndex(
                        (prev) => (prev + 1) % recomendaciones.length
                      )
                    }
                  >
                    →
                  </button>
                </div>
              </>
            )}
          </div>
        )}
      </div>
    </div>
  );
};

export default SearchSection;

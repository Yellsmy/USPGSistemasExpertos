import React, { useState } from 'react';
import './RecomendacionesGenerales.css';
import '../App.css';
import NavBar from './NavBar';
import MapSection from './Mapa';
import { obtenerRecomendacionesGenerales } from '../services/recomendacionesService';

const RecomendacionesGenerales = () => {
  const [preferencia, setPreferencia] = useState('');
  const [presupuesto, setPresupuesto] = useState('');
  const [temporada, setTemporada] = useState('');
  const [fechaViaje, setFechaViaje] = useState('');
  const [latitud, setLatitud] = useState(null);
  const [longitud, setLongitud] = useState(null);
  const [pais, setPais] = useState('');
  const [recomendaciones, setRecomendaciones] = useState([]);
  const [currentRecommendation, setCurrentRecommendation] = useState(0);

  // Función para buscar recomendaciones
  const buscarRecomendaciones = async () => {
    if (!latitud || !longitud || !pais) {
      alert("Por favor, selecciona tu ubicación en el mapa.");
      return;
    }

    const recomendacionesObtenidas = await obtenerRecomendacionesGenerales(
      preferencia, 
      presupuesto, 
      temporada, 
      latitud, 
      longitud, 
      pais, 
      fechaViaje
    );
    
    setRecomendaciones(recomendacionesObtenidas);
    setCurrentRecommendation(0);
  };

  // Funciones para navegar entre las recomendaciones
  const handleNextRecommendation = () => {
    setCurrentRecommendation((prev) => (prev + 1) % recomendaciones.length);
  };

  const handlePreviousRecommendation = () => {
    setCurrentRecommendation((prev) => (prev - 1 + recomendaciones.length) % recomendaciones.length);
  };

  const currentRec = recomendaciones[currentRecommendation];

  return (
    <div>
      {/* Sección 1: Encabezado */}
      <div className="main-page">
        <NavBar />
        <div className="content">
          <h1>Recomendaciones Generales</h1>
          <p>
          Buscar recomendaciones de viajes nunca había sido tan fácil. Ingresa las actividades de tu preferencia,
          el nivel de tu presupuesto destinado para este viaje, la temporada de tu interés, selecciona tu ubicación actual
          y la fecha en la que deseas viajar. Así de fácil obtendrás las mejores recomendaciones para el viaje de tus sueños.
          </p>
        </div>
      </div>
      {/* Sección 2: Consultas */}
      <div className="recommendations-page">
        {/* Primera Sub-Sección: Opciones que el usuario debe seleccionar */}
        <div className="selectors">
          <select value={preferencia} onChange={(e) => setPreferencia(e.target.value)}>
            <option value="">Preferencia</option>
            <option value="Cultura">Cultura</option>
            <option value="Playa">Playa</option>
            <option value="Escalada">Escalada</option>
            <option value="Naturaleza">Naturaleza</option>
          </select>

          <select value={presupuesto} onChange={(e) => setPresupuesto(e.target.value)}>
            <option value="">Presupuesto</option>
            <option value="Alto">Alto</option>
            <option value="Medio">Medio</option>
            <option value="Bajo">Bajo</option>
          </select>

          <select value={temporada} onChange={(e) => setTemporada(e.target.value)}>
            <option value="">Temporada</option>
            <option value="Verano">Verano</option>
            <option value="Invierno">Invierno</option>
            <option value="Primavera">Primavera</option>
            <option value="Otoño">Otoño</option>
          </select>
          <input type="date" value={fechaViaje} onChange={(e) => setFechaViaje(e.target.value)} />
          <button onClick={buscarRecomendaciones}>Buscar Recomendaciones</button>
        </div>

        {/* Segunda Sub-Sección: Mapa */}
        <div className="recommendations-body">
          <div className="map-section">
            <MapSection setLatitud={setLatitud} setLongitud={setLongitud} setPais={setPais} />
          </div>

          {/* Tercera Sub-Sección: Tarjetas con recomendaciones */}
          {recomendaciones.length > 0 ? (
            <div className="recommendation-card-container">
              <button onClick={handlePreviousRecommendation} className="arrow-button">←</button>
              <div className="recommendation-card-general">
                <h3>{currentRec.destino}</h3>
                <p>{currentRec.clima}</p>
                <p>Temperatura máxima: {currentRec.temperatura_max}</p>
                <p>Temperatura mínima: {currentRec.temperatura_min}</p>
                 {console.log(currentRec.imagen)}
                <img src={`http://127.0.0.1:5000${currentRec.imagen_url}`} alt={currentRec.destino} style={{ width: '100%', height: 'auto' }} />
                {currentRec.temporada !== temporada && (
                  <p className="warning-message">Por la temporada no se recomienda este destino.</p>
                )}
              </div>
              <button onClick={handleNextRecommendation} className="arrow-button">→</button>
            </div>
          ) : (
            <p>No hay recomendaciones disponibles</p>
          )}
        </div>
      </div>
    </div>
  );
  };

export default RecomendacionesGenerales;
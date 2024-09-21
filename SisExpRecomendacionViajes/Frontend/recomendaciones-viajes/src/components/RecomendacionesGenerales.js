// src/components/RecomendacionesGenerales.js
import React, { useState } from 'react';
import './RecomendacionesGenerales.css'; // Archivo CSS específico para esta pantalla
import '../App.css';
import NavBar from './NavBar';

const RecomendacionesGenerales = () => {
  // Estado para las recomendaciones (simulado por ahora)
  const [currentRecommendation, setCurrentRecommendation] = useState(0);
  const recommendations = [
    {
      place: "Puerto San José",
      country: "Guatemala",
      maxTemp: "39°",
      minTemp: "20°",
      image: "../assets/puerto-sanjose.jpg"
    },
    // Aquí podrían agregarse más recomendaciones simuladas
  ];

  const handleNextRecommendation = () => {
    setCurrentRecommendation((prev) => (prev + 1) % recommendations.length);
  };

  return (
    <div>
      {/* Sección 1: Encabezado con fondo de imagen */}
      <div className="main-page">
        <NavBar />
        <div className="content">
          <h1>Recomendaciones Generales</h1>
          <p>
          Buscar recomendaciones de viajes nunca había sido tan fácil. Ingresa las actividades de tu preferencia,
          el nivel de tu presupuesto destinado para este viaje, la temporada de tu interés, selecciona tu ubicación actual
          y la fecha en la que deseas viajar. Así de fácil obtendrás las mejores recomendaciones para el viaje de tus sueños
          </p>
        </div>
      </div>
        <div className="recommendations-page">
          {/* Primera Sub-Sección */}
          <div className="selectors">
            <select>
              <option value="">Preferencia</option>
              <option value="playa">Playa</option>
              <option value="escalar">Escalar</option>
              <option value="naturaleza">Naturaleza</option>
              <option value="aventura">Aventura</option>
            </select>

            <select>
              <option value="">Presupuesto</option>
              <option value="alto">Alto</option>
              <option value="medio">Medio</option>
              <option value="bajo">Bajo</option>
            </select>

            <select>
              <option value="">Temporada</option>
              <option value="verano">Verano</option>
              <option value="invierno">Invierno</option>
              <option value="primavera">Primavera</option>
              <option value="otoño">Otoño</option>
            </select>

            <input type="date" />
          </div>

          {/* Cuerpo de la página */}
        <div className="recommendations-body">
          {/* Mapa */}
          <div className="map-section">
            <h3>Selecciona tu ubicación</h3>
          </div>

          {/* Tarjeta de Recomendaciones */}
          <div className="recommendation-card-section">
            <div className="recommendation-card-general">
              <img src={recommendations[currentRecommendation].image} alt={recommendations[currentRecommendation].place} />
              <h3>{recommendations[currentRecommendation].place}</h3>
              <p>{recommendations[currentRecommendation].country}</p>
              <p>Temperatura máxima: {recommendations[currentRecommendation].maxTemp}</p>
              <p>Temperatura mínima: {recommendations[currentRecommendation].minTemp}</p>
            </div>
            <button onClick={handleNextRecommendation} className="next-button">→</button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default RecomendacionesGenerales;

import React, { useState } from 'react';
import './PersonalizedRecommendations.css';
import PersonalizedMapSection from './PersonalizedMapSection';
import SearchSection from './SearchSection';
import ItinerarySection from './ItinerarySection';

const PersonalizedRecommendations = () => {
  const [latitud, setLatitud] = useState(null);
  const [longitud, setLongitud] = useState(null);
  const [pais, setPais] = useState('No encontrado');
  const [itinerario, setItinerario] = useState(null);

  const actualizarItinerario = (nuevoItinerario) => {
    console.log('Actualizando itinerario:', nuevoItinerario); // Depuración
    setItinerario(nuevoItinerario);
  };

  return (
    <div className="personalized-recommendations-page">
      {/* Sección 1: Encabezado */}
      <header className="header">
        <h1>Recomendaciones Personalizadas</h1>
        <p>
          Bienvenido, aquí se mostrarán las recomendaciones basadas en tu historial y tus preferencias.
          Descubre destinos únicos adaptados a tus necesidades.
        </p>
      </header>

      {/* Contenedor para Sección 2 y Sección 3.1 */}
      <div className="section-group">
        <PersonalizedMapSection
          setLatitud={setLatitud}
          setLongitud={setLongitud}
          setPais={setPais}
          setItinerario={actualizarItinerario}
        />
      </div>

      {/* Contenedor para Sección 3.2 y Sección 3.3 */}
      <div className="section-group">
        <SearchSection
          latitud={latitud}
          longitud={longitud}
          pais={pais}
          setItinerario={actualizarItinerario}
        />
      </div>

      {/* Sección 4: Itinerario */}
      <ItinerarySection itinerario={itinerario} />
    </div>
  );
};

export default PersonalizedRecommendations;

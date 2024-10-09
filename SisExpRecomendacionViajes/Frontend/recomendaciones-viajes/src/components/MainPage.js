import React, { useRef } from 'react';
import NavBar from './NavBar';
import '../App.css';
import { useNavigate } from 'react-router-dom';

const MainPage = () => {
  const recommendationRef = useRef(null);
  const navigate = useNavigate();
  
  // Desplazamiendo suave
  const handleScrollToSection = () => {
    if (recommendationRef.current) {
      recommendationRef.current.scrollIntoView({
        behavior: 'smooth',
      });
    }
  };
  
  const handleGeneralClick = () => {
    navigate('/recomendaciones-generales');
  };

  return (
    <div>
      {/* Sección 1: Encabezado */}
      <div className="main-page">
        <NavBar />
        <div className="content">
          <h1>Recomendación de Viajes</h1>
          <p>
            Bienvenido al mejor recomendador de viajes donde podrás encontrar el viaje de tus sueños.
            Puedes hacer una búsqueda rápida o bien personalizada donde te daremos recomendaciones justo a tu medida.
            Lo que buscas lo encuentras aquí, viajalízate.
          </p>
          <button onClick={handleScrollToSection}>Explorar</button>
        </div>
      </div>
    
      {/* Sección 2: Tarjetas para recomendaciones */}
      <div ref={recommendationRef} className="recommendation-section">
        <h2>Explora entre nuestras distintas recomendaciones</h2>       
        <div className="recommendation-cards">
          <div className="recommendation-card general" onClick={handleGeneralClick}>
            <h3>Generales</h3>
            <p>Obtener recomendaciones nunca había sido tan fácil. Ingresa tus preferencias y explora las 
            recomendaciones que tenemos para ti.
            </p>
          </div>
          <div className="recommendation-card personalized">
            <h3>Personalizadas</h3>
            <p>Danos tus condiciones y te daremos soluciones. Ingresa detalles para que las recomendaciones se ajusten a tu medida, 
            y encuentra el viaje de tus sueños.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default MainPage;


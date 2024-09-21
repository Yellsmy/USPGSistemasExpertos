// src/components/MainPage.js
import React from 'react';
import NavBar from './NavBar';
import '../App.css';
import { useNavigate } from 'react-router-dom'; // Para manejar la navegación


const MainPage = () => {
  const navigate = useNavigate(); // Hook para manejar la navegación

  const handleGeneralClick = () => {
    navigate('/recomendaciones-generales'); // Navegamos a la nueva pantalla
  };
  return (
    <div>
      {/* Sección 1: Encabezado con fondo de imagen */}
      <div className="main-page">
        <NavBar />
        <div className="content">
          <h1>Recomendación de Viajes</h1>
          <p>
            Bienvenido al mejor recomendador de viajes donde podrás encontrar el viaje de tus sueños
            el cual no sabías que tenías hasta que te los recomendamos. Puedes hacer una búsqueda rápida 
            o bien podrás hacer una búsqueda personalizada donde te daremos las recomendaciones justo a tu medida.
            Lo que buscas lo encuentras aquí, viajalízate.
          </p>
          <button>Explorar</button>
        </div>
      </div>
    
      <div className="recommendation-section">
        <h2>Explora entre nuestras distintas recomendaciones</h2>       
        <div className="recommendation-cards">
          <div className="recommendation-card general" onClick={handleGeneralClick}>
            <h3>Generales</h3>
            <p>Obtener recomendaciones nunca había sido tan fácil! Ingresa tus preferencias y explora entre las 
            recomendaciones que tenemos para ti.
            </p>
          </div>
          <div className="recommendation-card personalized">
            <h3>Personalizadas</h3>
            <p>Danos tus condiciones y te daremos soluciones. Ingresa detalles para que las recomendaciones se ajusten a tu medida, 
            no te limites y encuentra el viaje de tus sueños.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
  };

export default MainPage;

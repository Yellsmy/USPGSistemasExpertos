import React, { useRef, useState } from 'react';
import NavBar from './NavBar';
import LoginModal from './LoginModal';
import { useNavigate } from 'react-router-dom';
import { fetchLogin } from '../services/authService'; // Importar correctamente el servicio
import '../App.css';

const MainPage = () => {
  const recommendationRef = useRef(null);
  const navigate = useNavigate();
  const [showLoginModal, setShowLoginModal] = useState(false);

  // Función para desplazarse a la sección de recomendaciones
  const handleScrollToSection = () => {
    if (recommendationRef.current) {
      recommendationRef.current.scrollIntoView({
        behavior: 'smooth',
      });
    }
  };

  // Navegación a recomendaciones generales
  const handleGeneralClick = () => {
    navigate('/recomendaciones-generales');
  };

  // Abrir y cerrar el modal
  const handleOpenLoginModal = () => setShowLoginModal(true);
  const handleCloseLoginModal = () => setShowLoginModal(false);

  // Manejo de inicio de sesión
  const handleLogin = async (username, password) => {
    try {
      const response = await fetchLogin(username, password); // Llamada al servicio con username
      localStorage.setItem('token', response.token); // Guarda el token en localStorage
      alert('Inicio de sesión exitoso');
      setShowLoginModal(false);
      navigate('/recomendaciones-personalizadas'); // Redirigir después del inicio de sesión
    } catch (error) {
      console.error('Error en el inicio de sesión:', error);
      alert(error.message || 'Hubo un problema al iniciar sesión. Por favor, inténtalo de nuevo.');
    }
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
            <p>
              Obtener recomendaciones nunca había sido tan fácil. Ingresa tus preferencias y explora las
              recomendaciones que tenemos para ti.
            </p>
          </div>
          <div className="recommendation-card personalized" onClick={handleOpenLoginModal}>
            <h3>Personalizadas</h3>
            <p>
              Danos tus condiciones y te daremos soluciones. Ingresa detalles para que las recomendaciones se ajusten a tu medida,
              y encuentra el viaje de tus sueños.
            </p>
          </div>
        </div>
      </div>

      {/* Modal de inicio de sesión */}
      {showLoginModal && (
        <LoginModal onClose={handleCloseLoginModal} onLogin={handleLogin} />
      )}
    </div>
  );
};

export default MainPage;

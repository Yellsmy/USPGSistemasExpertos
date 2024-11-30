import React, { useState } from 'react';
import './LoginModal.css';

const LoginModal = ({ onClose, onLogin }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (username && password) {
      onLogin(username, password); // Envía los datos al método `onLogin`
    } else {
      alert('Por favor, completa ambos campos.');
    }
  };

  return (
    <div className="login-modal">
      <div className="modal-content">
        <div className="welcome-section">
          <img
            src="https://via.placeholder.com/100" // Reemplázala por tu imagen real
            alt="Bienvenido"
            className="welcome-image"
          />
          <h2>Bienvenido</h2>
          <p>Debes iniciar sesión para acceder a las recomendaciones personalizadas</p>
        </div>
        <form onSubmit={handleSubmit}>
          <label htmlFor="username">Usuario</label>
          <input
            type="text"
            id="username"
            placeholder="Ingresa tu usuario"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />

          <label htmlFor="password">Contraseña</label>
          <input
            type="password"
            id="password"
            placeholder="Ingresa tu contraseña"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />

          <div className="button-container">
            <button type="submit" className="login-button">
              Iniciar Sesión
            </button>
            <button type="button" className="close-button" onClick={onClose}>
              Cerrar
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default LoginModal;

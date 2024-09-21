// src/components/NavBar.js
import React from 'react';
import './NavBar.css'; // Importa los estilos

const NavBar = () => {
  return (
    <div className="navbar">
      <ul>
        <li><a href="#">Nosotros</a></li>
        <li><a href="#"><span className="star">★</span> Califícanos</a></li>
        <li><a href="#"><span className="menu-icon">☰</span> Inicio</a></li>
      </ul>
    </div>
  );
};

export default NavBar;

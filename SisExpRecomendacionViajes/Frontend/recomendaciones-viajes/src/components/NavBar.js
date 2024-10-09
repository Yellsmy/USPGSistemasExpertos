import React, { useState } from 'react';
import './NavBar.css';
import AgregarRecomendacionModal from './AgregarRecomendacionModal';

const NavBar = () => {
  const [showModal, setShowModal] = useState(false);

  const handleOpenModal = () => {
    setShowModal(true);
  };

  const handleCloseModal = () => {
    setShowModal(false);
  };

  return (
    <div className="navbar">
      <ul>
        <li><a href="#">Nosotros</a></li>
        <li><a href="#"><span className="star">★</span> Califícanos</a></li>
        <li>
          <a href="#" onClick={handleOpenModal}>
            <span className="menu-icon">☰</span> Agregar
          </a>
        </li>
      </ul>
      {showModal && <AgregarRecomendacionModal onClose={handleCloseModal} />}
    </div>
  );
};

export default NavBar;

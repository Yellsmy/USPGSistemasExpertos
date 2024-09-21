// src/components/Selector.js
import React from 'react';

const Selector = ({ label, type = 'select' }) => {
  return (
    <div className="selector">
      <label>{label}</label>
      {type === 'select' ? (
        <select>
          <option value="">Selecciona {label.toLowerCase()}</option>
          {/* Opciones aquí */}
        </select>
      ) : (
        <input type={type} />
      )}
    </div>
  );
};

export default Selector;

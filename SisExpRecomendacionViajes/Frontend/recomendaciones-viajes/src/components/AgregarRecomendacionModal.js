import React, { useState } from 'react';
import './AgregarRecomendacionModal.css';
import { agregarRecomendacion } from '../services/agregarRecomendacionService';

const AgregarRecomendacionModal = ({ onClose }) => {
  const [formData, setFormData] = useState({
    destino: '',
    actividad: '',
    epoca: '',
    presupuesto: '',
    latitud: '',
    longitud: '',
    pais: '',
    imagen: null
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleImageChange = (e) => {
    setFormData({
      ...formData,
      imagen: e.target.files[0]
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Crea un objeto FormData para enviar los datos
    const formDataToSend = new FormData();
    formDataToSend.append('destino', formData.destino); 
    formDataToSend.append('actividad', formData.actividad);
    formDataToSend.append('epoca', formData.epoca);
    formDataToSend.append('presupuesto', formData.presupuesto);
    formDataToSend.append('latitud', formData.latitud);
    formDataToSend.append('longitud', formData.longitud);
    formDataToSend.append('pais', formData.pais);
    formDataToSend.append('imagen', formData.imagen);

    try {
      const result = await agregarRecomendacion(formDataToSend);
      alert('Recomendación agregada con éxito');
      console.log(result);
      onClose();
    } catch (error) {
      alert('Hubo un error al agregar la recomendación');
      console.error('Error:', error);
    }
  };

  return (
    <div className="modal">
      <div className="modal-content">
        <span className="close" onClick={onClose}>&times;</span>
        <h2>Agregar nueva recomendación</h2>
        <form onSubmit={handleSubmit}>
          {/* Destino */}
          <label>Destino:</label>
          <input
            type="text"
            name="destino"
            value={formData.destino}
            onChange={handleChange}
            required
          />

          {/* Preferencia (Actividad) */}
          <label>Preferencia (Actividad):</label>
          <div className="radio-group">
            <label>
              <input
                type="radio"
                name="actividad"
                value="Cultura"
                checked={formData.actividad === 'Cultura'}
                onChange={handleChange}
                required
              />
              Cultura
            </label>
            <label>
              <input
                type="radio"
                name="actividad"
                value="Playa"
                checked={formData.actividad === 'Playa'}
                onChange={handleChange}
                required
              />
              Playa
            </label>
            <label>
              <input
                type="radio"
                name="actividad"
                value="Escalada"
                checked={formData.actividad === 'Escalada'}
                onChange={handleChange}
                required
              />
              Escalada
            </label>
            <label>
              <input
                type="radio"
                name="actividad"
                value="Naturaleza"
                checked={formData.actividad === 'Naturaleza'}
                onChange={handleChange}
                required
              />
              Naturaleza
            </label>
          </div>

          {/* Temporada */}
          <label>Temporada:</label>
          <div className="radio-group">
            <label>
              <input
                type="radio"
                name="epoca"
                value="Invierno"
                checked={formData.epoca === 'Invierno'}
                onChange={handleChange}
                required
              />
              Invierno
            </label>
            <label>
              <input
                type="radio"
                name="epoca"
                value="Verano"
                checked={formData.epoca === 'Verano'}
                onChange={handleChange}
                required
              />
              Verano
            </label>
            <label>
              <input
                type="radio"
                name="epoca"
                value="Otoño"
                checked={formData.epoca === 'Otoño'}
                onChange={handleChange}
                required
              />
              Otoño
            </label>
            <label>
              <input
                type="radio"
                name="epoca"
                value="Primavera"
                checked={formData.epoca === 'Primavera'}
                onChange={handleChange}
                required
              />
              Primavera
            </label>
          </div>

          {/* Presupuesto */}
          <label>Presupuesto:</label>
          <div className="radio-group">
            <label>
              <input
                type="radio"
                name="presupuesto"
                value="Alto"
                checked={formData.presupuesto === 'Alto'}
                onChange={handleChange}
                required
              />
              Alto
            </label>
            <label>
              <input
                type="radio"
                name="presupuesto"
                value="Medio"
                checked={formData.presupuesto === 'Medio'}
                onChange={handleChange}
                required
              />
              Medio
            </label>
            <label>
              <input
                type="radio"
                name="presupuesto"
                value="Bajo"
                checked={formData.presupuesto === 'Bajo'}
                onChange={handleChange}
                required
              />
              Bajo
            </label>
          </div>

          {/* Latitud */}
          <label>Latitud:</label>
          <input
            type="number"
            name="latitud"
            value={formData.latitud}
            onChange={handleChange}
            required
          />

          {/* Longitud */}
          <label>Longitud:</label>
          <input
            type="number"
            name="longitud"
            value={formData.longitud}
            onChange={handleChange}
            required
          />

          {/* País */}
          <label>País:</label>
          <input
            type="text"
            name="pais"
            value={formData.pais}
            onChange={handleChange}
            required
          />

          {/* Imagen */}
          <label>Imagen:</label>
          <input
            type="file"
            name="imagen"
            onChange={handleImageChange}
            accept="image/*"
            required
          />

          {/* Botones */}
          <div className="button-container">
            <button className="cancel-button" onClick={onClose}>Cancelar</button>
            <button type="submit">Agregar</button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default AgregarRecomendacionModal;

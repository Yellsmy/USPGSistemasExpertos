import React from 'react';
import './SearchCriteria.css';

const SearchCriteria = () => {
  return (
    <div className="search-criteria">
      <h3>Criterios de búsqueda</h3>
      <form>
        <label htmlFor="preference">Preferencia</label>
        <select id="preference">
          <option value="">Selecciona...</option>
          <option value="Cultura">Cultura</option>
          <option value="Playa">Playa</option>
          <option value="Escalada">Escalada</option>
          <option value="Naturaleza">Naturaleza</option>
        </select>

        <label htmlFor="budget">Presupuesto</label>
        <select id="budget">
          <option value="">Selecciona...</option>
          <option value="Bajo">Bajo</option>
          <option value="Medio">Medio</option>
          <option value="Alto">Alto</option>
        </select>

        <label htmlFor="travel-date">Fecha de viaje</label>
        <input type="date" id="travel-date" />

        <label htmlFor="people">Cantidad de personas</label>
        <input type="number" id="people" min="1" max="20" />
      </form>
    </div>
  );
};

export default SearchCriteria;

/*import React, { useEffect, useState } from 'react';
import { obtenerDetalleDestino } from '../../services/recommendationsService';
import './ItinerarySection.css';

const ItinerarySection = ({ destinationId }) => {
  const [destination, setDestination] = useState(null);

  useEffect(() => {
    const fetchItinerary = async () => {
      try {
        const data = await obtenerDetalleDestino(destinationId);
        setDestination(data.destino);
      } catch (error) {
        console.error('Error al cargar el itinerario:', error);
      }
    };

    if (destinationId) fetchItinerary();
  }, [destinationId]);

  if (!destination) return <p>Cargando itinerario...</p>;

  const { itinerario } = destination;

  return (
    <div className="itinerary-section">
      <h2>Itinerario</h2>

      <h3>Lista de Actividades</h3>
      <div className="timeline">
        {itinerario.actividades.map((actividad, index) => (
          <div key={index} className="timeline-item">
            <p>{actividad.name}</p>
            <span>Duración: {actividad.duration} horas</span>
          </div>
        ))}
      </div>

      <h3>Alojamiento</h3>
      <div className="card">
        <img src="/path/to/accommodation.jpg" alt="Alojamiento" />
        <div>
          <p>Costo Alojamiento:</p>
          <p>${itinerario.alojamiento.price_per_night}</p>
        </div>
      </div>

      <h3>Comida</h3>
      {itinerario.comida.map((comida, index) => (
        <div key={index} className="card">
          <img src="/path/to/food.jpg" alt="Comida" />
          <div>
            <p>Costo Comida:</p>
            <p>${comida.price_per_person}</p>
          </div>
        </div>
      ))}

      <div className="total-cost">
        <p>En base a los costos obtenidos, el costo del viaje será de:</p>
        <h2>${itinerario.costo_total}</h2>
      </div>
    </div>
  );
};

export default ItinerarySection;
*/

import React from 'react';
import './ItinerarySection.css';

const ItinerarySection = ({ itinerario }) => {
  // Siempre renderizar el contenedor principal para evitar errores en `scrollIntoView`
  return (
    <div className="section-4" id="section-itinerary">
      <h2>Itinerario del Destino Seleccionado</h2>
      {itinerario ? (
        <div className="itinerary">
          <div className="timeline">
            <h3>Actividades</h3>
            {itinerario.actividades && itinerario.actividades.length > 0 ? (
              itinerario.actividades.map((actividad, index) => (
                <div className="timeline-item" key={index}>
                  <p>Actividad: {actividad.name}</p>
                  <p>Duración: {actividad.duration} horas</p>
                  <p>Precio: ${actividad.price}</p>
                </div>
              ))
            ) : (
              <p>No hay actividades disponibles.</p>
            )}
          </div>
          <div className="accommodation-food">
            <h3>Alojamiento</h3>
            {itinerario.alojamiento ? (
              <div className="card">
                <p>Alojamiento: {itinerario.alojamiento.type}</p>
                <p>Precio por noche: ${itinerario.alojamiento.price_per_night}</p>
              </div>
            ) : (
              <p>No hay información sobre alojamiento.</p>
            )}
            <h3>Comida</h3>
            {itinerario.comida && itinerario.comida.length > 0 ? (
              itinerario.comida.map((comidaItem, index) => (
                <div className="card" key={index}>
                  <p>Comida: {comidaItem.name}</p>
                  <p>Precio por persona: ${comidaItem.price_per_person}</p>
                </div>
              ))
            ) : (
              <p>No hay información sobre comida.</p>
            )}
          </div>
          {itinerario.costo_total ? (
            <div className="total-cost">
              <h3>Costo Total</h3>
              <p>${itinerario.costo_total}</p>
            </div>
          ) : (
            <p>No se pudo calcular el costo total.</p>
          )}
        </div>
      ) : (
        <p>No hay información disponible sobre el itinerario. Selecciona un destino para verlo.</p>
      )}
    </div>
  );
};

export default ItinerarySection;

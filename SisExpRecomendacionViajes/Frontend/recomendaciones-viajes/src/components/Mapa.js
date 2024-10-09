import React, { useEffect, useRef } from 'react';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

const Mapa = ({ setLatitud, setLongitud, setPais }) => {
  const mapRef = useRef(null); 

  useEffect(() => {
    if (!mapRef.current) {
      // Inicializa el mapa solo si no ha sido inicializado
      mapRef.current = L.map('map').setView([14.634915, -90.506882], 10);

      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
      }).addTo(mapRef.current);

      let marker;

      // Obtiene la latitud y longitud al hacer clic en el mapa
      mapRef.current.on('click', function (e) {
        const lat = e.latlng.lat;
        const lng = e.latlng.lng;

        // Actualiza los estados de latitud y longitud
        setLatitud(lat.toFixed(6));
        setLongitud(lng.toFixed(6));

        // Remueve marcador previo si existe
        if (marker) {
          mapRef.current.removeLayer(marker);
        }

        // Agrega un nuevo marcador
        marker = L.marker([lat, lng]).addTo(mapRef.current);

        // API de Nominatim para obtener la dirección a partir de las coordenadas
        fetch(`https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=${lat}&lon=${lng}`)
          .then(response => response.json())
          .then(data => {
            const country = data.address.country || 'No encontrado';
            setPais(country);
          })
          .catch(error => console.log('Error al obtener el país:', error));
      });
    }
  }, [setLatitud, setLongitud, setPais]);

  return <div id="map" style={{ height: '400px', width: '100%' }}></div>;
};

export default Mapa;



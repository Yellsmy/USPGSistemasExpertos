import React, { useEffect, useRef } from 'react';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

const PersonalizedMap = ({ setLatitud, setLongitud, setPais }) => {
  const mapRef = useRef(null);

  useEffect(() => {
    if (!mapRef.current) {
      mapRef.current = L.map('personalized-map').setView([14.634915, -90.506882], 10);

      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors',
      }).addTo(mapRef.current);

      let marker;

      mapRef.current.on('click', (e) => {
        const lat = e.latlng.lat;
        const lng = e.latlng.lng;

        console.log('Mapa clicado:', { lat, lng });

        setLatitud(lat.toFixed(6));
        setLongitud(lng.toFixed(6));

        if (marker) {
          mapRef.current.removeLayer(marker);
        }

        marker = L.marker([lat, lng]).addTo(mapRef.current);

        // API de Nominatim para obtener el país
        fetch(`https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=${lat}&lon=${lng}`)
          .then((response) => response.json())
          .then((data) => {
            const country = data.address.country || 'No encontrado';
            console.log('País obtenido:', country);
            setPais(country);
          })
          .catch((error) => console.error('Error al obtener el país:', error));
      });
    }
  }, [setLatitud, setLongitud, setPais]);

  return <div id="personalized-map" style={{ height: '400px', width: '100%' }}></div>;
};

export default PersonalizedMap;


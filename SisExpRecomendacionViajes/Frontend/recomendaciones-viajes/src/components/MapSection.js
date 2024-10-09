import React, { useState, useEffect } from 'react';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import './RecomendacionesGenerales.css';

const MapSection = () => {
  const [latitud, setLatitud] = useState(null);
  const [longitud, setLongitud] = useState(null);
  const [pais, setPais] = useState('No encontrado');
  const [map, setMap] = useState(null);
  const [marker, setMarker] = useState(null);

  useEffect(() => {
    // Inicializamos el mapa cuando el componente se monta
    const mapInstance = L.map('map').setView([14.634915, -90.506882], 10);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '© OpenStreetMap contributors'
    }).addTo(mapInstance);

    setMap(mapInstance);

    return () => {
      mapInstance.remove();
    };
  }, []);

  // Función que se ejecuta cuando el usuario hace clic en el mapa
  const handleMapClick = (e) => {
    const lat = e.latlng.lat;
    const lng = e.latlng.lng;

    setLatitud(lat.toFixed(6));
    setLongitud(lng.toFixed(6));

    // Remueve el marcador previo si existe
    if (marker) {
      map.removeLayer(marker);
    }

    // Se agrega un nuevo marcador en la ubicación seleccionada
    const newMarker = L.marker([lat, lng]).addTo(map);
    setMarker(newMarker);

    // API de Nominatim para obtener el país a partir de las coordenadas
    fetch(`https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=${lat}&lon=${lng}`)
      .then((response) => response.json())
      .then((data) => {
        const country = data.address.country || 'No encontrado';
        setPais(country);
      })
      .catch((error) => {
        console.error('Error al obtener el país:', error);
      });
  };

  useEffect(() => {
    if (map) {
      map.on('click', handleMapClick);
    }
  }, [map, marker]);

  return (
    <div className="recommendations-body">
      <h3>Selecciona tu ubicación en el mapa</h3>
      <div id="map" ></div>
    </div>
  );
};

export default MapSection;

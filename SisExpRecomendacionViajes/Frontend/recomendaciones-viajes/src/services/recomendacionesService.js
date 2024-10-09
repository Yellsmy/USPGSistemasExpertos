export const obtenerRecomendacionesGenerales = async (preferencia, presupuesto, temporada, latitud, longitud, pais, fecha_viaje) => {
  const API_URL = 'http://127.0.0.1:5000/recomendaciones/buscar';
  const body = {
    preferencia,
    temporada,
    presupuesto,
    latitud,
    longitud,
    pais,
    fecha_viaje
  };

  try {
    const response = await fetch(API_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(body)
    });
    
    if (!response.ok) {
      throw new Error(`Error en la respuesta del servidor: ${response.status}`);
    }

    const data = await response.json();
    return data.recomendaciones || [];
  } catch (error) {
    console.error("Error al obtener las recomendaciones:", error);
    return [];
  }
};

const API_BASE_URL = 'http://127.0.0.1:5000'; // URL base de la API

// Función para obtener el token JWT desde el almacenamiento local
const obtenerToken = () => {
  const token = localStorage.getItem('token');
  if (!token) {
    throw new Error('Token de autenticación no disponible');
  }
  return token;
};

// Función para obtener recomendaciones basadas en el historial
export const obtenerRecomendacionDestacada = async () => {
  try {
    const token = obtenerToken(); // Obtener el token almacenado
    const response = await fetch(`${API_BASE_URL}/recommendations/personalized/user-recommendations`, {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.message || `Error HTTP: ${response.status}`);
    }

    const data = await response.json();
    return data.recomendaciones; // Devuelve la lista de recomendaciones
  } catch (error) {
    console.error('Error al obtener la recomendación destacada:', error);
    throw error;
  }
};

// Función para buscar recomendaciones personalizadas
export const buscarRecomendacionesPersonalizadas = async ({
  preferencia,
  presupuesto,
  latitud,
  longitud,
  pais,
  fecha_viaje,
  people_count,
}) => {
  try {
    const response = await fetch(`${API_BASE_URL}/recommendations/personalized`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        preferencia,
        presupuesto,
        latitud,
        longitud,
        pais,
        fecha_viaje,
        people_count,
      }),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.message || `Error HTTP: ${response.status}`);
    }

    const data = await response.json();
    return data.recomendaciones; // Devuelve la lista de recomendaciones
  } catch (error) {
    console.error('Error al buscar recomendaciones:', error);
    throw error;
  }
};


// Función para registrar un destino en el historial
export const seleccionarRecomendacion = async (recommendationId) => {
  try {
    const token = localStorage.getItem('token'); // Obtener token JWT del almacenamiento local
    if (!token) {
      throw new Error('Token de autenticación no disponible');
    }

    const response = await fetch(`${API_BASE_URL}/recommendations/personalized/select`, {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ recommendation_id: recommendationId }),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.message || `Error HTTP: ${response.status}`);
    }

    const data = await response.json();
    return data.message; // Devuelve el mensaje de confirmación
  } catch (error) {
    console.error('Error al seleccionar la recomendación:', error);
    throw error;
  }
};

// Función para buscar una recomendación específica
export const buscarRecomendacionEspecifica = async (destinationId) => {
  try {
    const token = obtenerToken(); // Obtener el token almacenado
    const response = await fetch(`${API_BASE_URL}/recommendations/personalized/destination/${destinationId}`, {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.message || `Error HTTP: ${response.status}`);
    }

    const data = await response.json();
    return data; // Devuelve los detalles de la recomendación
  } catch (error) {
    console.error('Error al buscar recomendación específica:', error);
    throw error;
  }
};
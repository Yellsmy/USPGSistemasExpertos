export const obtenerRecomendacionesPersonalizadas = async (params) => {
    const API_URL = 'http://127.0.0.1:5000/personalized';
    const token = localStorage.getItem('token');
  
    try {
      const response = await fetch(API_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(params),
      });
  
      if (!response.ok) {
        throw new Error('Error al buscar recomendaciones');
      }
  
      return await response.json();
    } catch (error) {
      console.error(error);
      throw error;
    }
  };
  
export const obtenerDetalleDestino = async (destinationId) => {
    const API_URL = `http://127.0.0.1:5000/personalized/destination/${destinationId}`;
    const token = localStorage.getItem('token');

    try {
        const response = await fetch(API_URL, {
        method: 'GET',
        headers: {
            Authorization: `Bearer ${token}`,
        },
        });

        if (!response.ok) {
        throw new Error('Error al obtener detalles del destino');
        }

        return await response.json();
    } catch (error) {
        console.error(error);
        throw error;
    }
};

export const obtenerRecomendacionesBasadasEnHistorial = async () => {
    const API_URL = 'http://127.0.0.1:5000/personalized/user-recommendations';
    const token = localStorage.getItem('token');
  
    try {
      const response = await fetch(API_URL, {
        method: 'GET',
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
  
      if (!response.ok) {
        throw new Error('Error al obtener el historial');
      }
  
      return await response.json();
    } catch (error) {
      console.error(error);
      throw error;
    }
  };
  
  
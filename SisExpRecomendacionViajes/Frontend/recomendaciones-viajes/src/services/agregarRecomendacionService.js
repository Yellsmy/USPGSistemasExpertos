const API_URL = 'http://127.0.0.1:5000/recomendaciones';

export const agregarRecomendacion = async (formData) => {
  try {
    const response = await fetch(API_URL, {
      method: 'POST',
      body: formData,
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.mensaje || 'Error al agregar la recomendación');
    }

    return await response.json();
  } catch (error) {
    console.error('Error en el servicio:', error);
    throw error;
  }
};

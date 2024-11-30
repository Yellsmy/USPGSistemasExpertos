const API_URL = 'http://127.0.0.1:5000/auth/login';

export const fetchLogin = async (username, password) => {
  try {
    const response = await fetch(API_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }), // Cambiado a username
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.message || 'Error al iniciar sesión');
    }
    const token = localStorage.getItem('token');

    if (token) {
        console.log('Token recuperado:', token);
    } else {
        console.log('No se encontró el token');
    }
    const data = await response.json();
    return data; // { token: "JWT_TOKEN" }
    

  } catch (error) {
    console.error('Error en fetchLogin:', error);
    throw error;
  }
};

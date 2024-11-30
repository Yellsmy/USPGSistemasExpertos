const API_URL = 'http://localhost/Facturacion/BackendFacturacion'; 

export const getPrecios = async () => {
    try {
        const response = await fetch(`${API_URL}/precios/mostrar`);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching tipos de combustible:', error);
        throw error;
    }
};

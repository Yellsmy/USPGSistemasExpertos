const API_URL = 'http://localhost/Facturacion/BackendFacturacion'; 

export const crearFactura = async (invoiceData) => {
    try {
        const response = await fetch(`${API_URL}/factura/crear`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(invoiceData),
        });

        if (!response.ok) {
            throw new Error(`Network response was not ok: ${response.statusText}`);
        }

        const responseText = await response.text();

        try {
            const data = JSON.parse(responseText);
            console.log("En el consumo de la api:", data)
            return data;
        } catch (e) {
            throw new Error(`La respuesta de la API no es JSON válido: ${responseText}`);
        }

    } catch (error) {
        console.error('Error al llamar a la API:', error);
        throw error;
    }

};

export const getFacturaPorId = async (id_factura_detalle) => {
    console.log("Dentro del service. ID recibido:", id_factura_detalle)
    try {
        console.log(JSON.stringify({ "id_factura_detalle":id_factura_detalle }));
        const response = await fetch(`${API_URL}/factura/one`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ "id_factura_detalle":id_factura_detalle })
            });

        if (!response.ok) {
            const errorText = await response.text();
            console.error('Network response was not ok:', errorText);
            throw new Error('Network response was not ok: ' + errorText);
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching factura:', error);
        throw error;
    }
};

export const getAllFacturas = async () => {
    try {
        const response = await fetch(`${API_URL}/factura/all`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (!response.ok) {
            throw new Error(`Network response was not ok: ${response.statusText}`);
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching facturas:', error);
        throw error;
    }
};

export const busquedaFactura = async (numero_factura) => {
    console.log("Dentro del service. Número de factura recibido:", numero_factura)
    try {
        const response = await fetch(`${API_URL}/factura/busqueda`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ "numero_factura": numero_factura })
        });

        if (!response.ok) {
            const errorText = await response.text();
            console.error('Network response was not ok:', errorText);
            throw new Error('Network response was not ok: ' + errorText);
        }

        const data = await response.json();
        console.log("Dentro de busqueda. Número de id devuelto:", data[0].id_factura_detalle)
        const dataOne = await getFacturaPorId(data[0].id_factura_detalle);
        console.log("datos factura recibidos. ID devuelto de la factura", dataOne.id_factura_detalle)
        return dataOne;
    } catch (error) {
        console.error('Error fetching factura:', error);
        throw error;
    }
};
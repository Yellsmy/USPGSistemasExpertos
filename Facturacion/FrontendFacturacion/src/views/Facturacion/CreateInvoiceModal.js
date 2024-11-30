
import { loadFacturas } from '../Facturacion/FacturacionView.js';
import { showPDF } from '../PDF/PDFView.js';
import { crearFactura } from '../../services/FacturacionService.js';

export function openCreateInvoiceModal() {
    const modalHTML = `
        <div id="createFormModal" class="modal">
            <div class="modal-content">
                <span class="close-button">×</span>
                <h2>Crear Factura</h2>
                <form id="createInvoiceForm">
                    <label for="nit">NIT o CF:</label>
                    <input type="text" id="nit" name="nit">
                    <label for="monto_consumo">Monto:</label>
                    <input type="number" id="monto_consumo" name="monto_consumo">
                    <div class="radio-buttons">
                        <input type="radio" id="diesel" name="tipo_combustible" value="Diesel"><label for="diesel">Diésel</label>
                        <input type="radio" id="premium" name="tipo_combustible" value="Premium"><label for="premium">Premium</label>
                        <input type="radio" id="super" name="tipo_combustible" value="Super"><label for="super">Súper</label>
                        <input type="radio" id="regular" name="tipo_combustible" value="Regular"><label for="regular">Regular</label>
                    </div>
                    <label for="paymentMethod">Método de Pago:</label>
                    <div class="radio-buttons">
                        <input type="radio" id="tarjeta" name="forma_pago" value="tarjeta"><label for="tarjeta">Tarjeta</label>
                        <input type="radio" id="efectivo" name="forma_pago" value="efectivo"><label for="efectivo">Efectivo</label>
                    </div>
                    <button type="submit">Guardar</button>
                </form>
            </div>
        </div>
    `;
    document.body.insertAdjacentHTML('beforeend', modalHTML);

    document.getElementById('createInvoiceForm').addEventListener('submit', async function(event) {
        event.preventDefault(); 

        const nit = document.getElementById('nit').value;
        const monto_consumo = document.getElementById('monto_consumo').value;
        const tipo_combustible = document.querySelector('input[name="tipo_combustible"]:checked').value;
        const forma_pago = document.querySelector('input[name="forma_pago"]:checked').value;

        const invoiceData = {
            nit: nit,
            monto_consumo: monto_consumo,
            tipo_combustible: tipo_combustible,
            forma_pago: forma_pago
        };

        console.log("Datos del formulario:", invoiceData);
        
        try {
            const data = await crearFactura(invoiceData);
            console.log('Respuesta de la API:', data);
            if (data.error) {
                alert('Error al crear la factura: ' + data.error);
            } else {
                alert('Factura creada exitosamente.');
                document.getElementById('createFormModal').style.display = 'none';
                // Asegúrate de que data contiene el ID de la factura creada
                console.log("Id de la factura creada:", data)
                if (data) {
                    await showPDF(data);
                } else {
                    console.error('No se pudo obtener el ID de la factura creada.');
                }
                await loadFacturas();
            }
        } catch (error) {
            alert('Error al crear la factura.');
        }
    });

    document.querySelector('.close-button').addEventListener('click', function() {
        document.getElementById('createFormModal').style.display = 'none';
    });

    window.onclick = function(event) {
        if (event.target == document.getElementById('createFormModal')) {
            document.getElementById('createFormModal').style.display = 'none';
        }
    };
}


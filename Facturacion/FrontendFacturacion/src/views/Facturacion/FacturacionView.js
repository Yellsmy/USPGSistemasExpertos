import { openCreateInvoiceModal } from './CreateInvoiceModal.js';
import { generatePDF } from '../../components/PDFGenerador.js';
import { getAllFacturas, busquedaFactura } from '../../services/FacturacionService.js';

export function showFacturacion() {
    const mainContent = document.getElementById('main-content');
    mainContent.innerHTML = `
    <div class="main-content">
        <div class="table-container" id="table-container">
            <div class="search-container">
                <input type="text" placeholder="NIT o número de Factura" id="searchFactura">
                <button type="button" id="searchButton">Buscar</button>
            </div>
            <table class="facturas-table">
                <thead>
                    <tr>
                        <th>Número de factura</th>
                        <th>Cantidad (Galón)</th>
                        <th>Total (Q)</th>
                    </tr>
                </thead>
                <tbody id="facturasTable">
                    <!-- Los datos de las facturas se cargarán aquí -->
                </tbody>
            </table>
            <button id="createInvoiceButton" class="btn btn-primary">Crear Nueva Factura</button>
        </div>
        <div class="pdf-viewer" id="pdf-container">
            <button id="closePDFButton" class="btn btn-secondary">Cerrar PDF</button>
            <!-- El visor de PDF se mostrará aquí -->
        </div>
    </div>
    `;

    document.getElementById('createInvoiceButton').addEventListener('click', openCreateInvoiceModal);
    document.getElementById('searchButton').addEventListener('click', handleSearch);
    document.getElementById('closePDFButton').addEventListener('click', closePDFViewer);
    loadFacturas();  
}

function closePDFViewer() {
    const pdfContainer = document.getElementById('pdf-container');
    const tableContainer = document.getElementById('table-container');
    pdfContainer.style.display = 'none';
    tableContainer.style.flex = '1';
}

export async function loadFacturas() {
    try {
        const facturas = await getAllFacturas();
        const lastFiveFacturas = facturas.slice(-10); // Selecciona las últimas 10 facturas

        const tableBody = document.getElementById('facturasTable');
        tableBody.innerHTML = ''; 
        lastFiveFacturas.forEach(factura => {
            let row = tableBody.insertRow();
            row.insertCell(0).innerHTML = factura.numero_factura;
            row.insertCell(1).innerHTML = factura.cantidad_consumo;
            row.insertCell(2).innerHTML = factura.monto_consumo;
        });
    } catch (error) {
        console.error('Error cargando facturas:', error);
    }
}

function initFacturacionEvents() {
    const searchInput = document.getElementById('searchFactura');
    const createButton = document.getElementById('createInvoiceButton');

    if (searchInput) {
        searchInput.addEventListener('input', handleSearch);
    }

    if (createButton) {
        createButton.addEventListener('click', openCreateInvoiceModal);
    }
}

async function handleSearch() {
    const searchInput = document.getElementById('searchFactura').value;
    
    try {
        const factura = await busquedaFactura(searchInput);
        if (factura) {
            const pdfBase64 = await generatePDF(factura.id_factura_detalle); // Usar el valor del input para generar el PDF
            if (pdfBase64) {
                const pdfContainer = document.getElementById('pdf-container');
                const tableContainer = document.getElementById('table-container');
                pdfContainer.style.display = 'flex';
                tableContainer.style.flex = '2';
                pdfContainer.innerHTML = `<button id="closePDFButton" class="btn btn-secondary">Cerrar PDF</button>
                <object
                    width="100%"
                    height="100%"
                    type="application/pdf"
                    data="${pdfBase64}">
                    <p>Tu navegador no soporta la visualización de PDF. Por favor, descarga el PDF <a href="${pdfBase64}">aquí</a>.</p>
                </object>`;
                document.getElementById('closePDFButton').addEventListener('click', closePDFViewer);
            } else {
                console.error('Error al generar el PDF.');
            }
        } else {
            console.error('No se encontró ninguna factura.');
            const pdfContainer = document.getElementById('pdf-container');
            pdfContainer.innerHTML = '<p>No se encontró ninguna factura con el criterio de búsqueda proporcionado.</p>';
        }
    } catch (error) {
        console.error('Error en la búsqueda de factura:', error);
    }
}

document.addEventListener('DOMContentLoaded', function() {
    initFacturacionEvents();  
    loadFacturas();  
});

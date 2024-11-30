import { generatePDF } from '../../components/PDFGenerador.js';

export async function showPDF(facturaId) {
    try {
        const pdfBase64 = await generatePDF(facturaId);
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
    } catch (error) {
        console.error('Error al buscar la factura:', error);
    }
}

function closePDFViewer() {
    const pdfContainer = document.getElementById('pdf-container');
    const tableContainer = document.getElementById('table-container');
    pdfContainer.style.display = 'none';
    tableContainer.style.flex = '1';
}


import { getFacturaPorId } from '../services/FacturacionService.js';

export async function generatePDF(id_factura) {
    try {
        const data = await getOneFactura(id_factura);

        console.log('Datos obtenidos:', data);

        // Configuración del documento PDF con tamaño personalizado
        const doc = new jsPDF({
            orientation: 'portrait',
            unit: 'mm',
            format: [200, 450] // Tamaño de la página: 80mm de ancho por 200mm de alto
        });

       // Información del emisor de la factura
       doc.setFont("helvetica", "bold");
       doc.setFontSize(14);
       doc.text("G500", 35, 10, { align: "center" }); // Logo o nombre de la estación
       doc.setFontSize(10);
       doc.text(data.nombre_estacion, 35, 20, { align: "center" });

       // Dirección y otros detalles
       doc.setFont("helvetica", "normal");
       doc.setFontSize(8);
       doc.text(`Dirección: ${data.direccion_estacion}`, 10, 30);
       doc.text(`Teléfono: ${data.telefono_estacion}`, 10, 35);
       doc.text(`Código: ${data.codigo_estacion}`, 10, 40);

       // Nota y folio
       doc.setFont("helvetica", "bold");
       doc.setFontSize(10);
       doc.text("***** ORIGINAL *****", 35, 50, { align: "center" });
       doc.text(`SERIE: ${data.serie}`, 35, 55, { align: "center" });
       doc.text(`NOTA #${data.numero_factura}`, 35, 60, { align: "center" });



       // Información del cliente
       doc.setFont("helvetica", "bold");
       doc.setFontSize(10);
       doc.text("Facturado a:", 10, 70);
       doc.setFont("helvetica", "normal");
       doc.setFontSize(8);
       doc.text(`FECHA: ${data.fecha_hora}`, 10, 75);
       doc.text(`NIT: ${data.nit}`, 10, 80);
       doc.text(data.nombre_cliente, 10, 85);
       doc.text(`Forma de pago: ${data.forma_pago}`, 10, 90);

       // Detalles de la factura
       const columnXPositions = [5, 25, 40, 55]; // Distribuir uniformemente a lo largo del ancho de 200mm
        doc.text("Descripción", columnXPositions[0], 100);
        doc.text("Cantidad", columnXPositions[1], 100);
        doc.text("Precio", columnXPositions[2], 100);
        doc.text("Total", columnXPositions[3], 100);

        // Líneas de los productos o servicios
        doc.setFont("helvetica", "normal");
        doc.setFontSize(8);
        doc.text(data.tipo_combustible, columnXPositions[0], 105);
        doc.text(`${data.cantidad_consumo}`, columnXPositions[1], 105);
        doc.text(`Q${data.precio}`, columnXPositions[2], 105);
        doc.text(`Q${data.monto_consumo}`, columnXPositions[3], 105);


       // Suma total
       doc.setFont("helvetica", "bold");
       doc.setFontSize(10);
       doc.text("Total a pagar", 10, 115);
       doc.text(`Q${data.monto_consumo}`, 40, 115);

       // Términos y condiciones
       doc.setFont("helvetica", "italic");
       doc.setFontSize(8);
       doc.text("Gracias por su compra.", 35, 130, { align: "center" });
       doc.text("Términos y condiciones aplican.", 35, 135, { align: "center" });

       // Obtener el documento PDF como base64
       const pdfBase64 = doc.output('datauristring');
        
        return pdfBase64; 
    } catch (error) {
        console.error('Error generando el PDF:', error);
        return null;
    }
}

async function getOneFactura(id_factura) {
    const data = await getFacturaPorId(id_factura);
    return data;
}

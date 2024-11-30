
import { getPrecios } from '../../services/PreciosService';

export async function showPrecios() {
    const mainContent = document.getElementById('main-content');

    try {
        const precios = await getPrecios();
        
        let tablaContenido = precios.map(precio =>
            `<tr>
                <td>${precio.Tipo}</td>
                <td>Q.${precio.Precio}</td>
            </tr>`
        ).join('');

        mainContent.innerHTML = `
            <div class="precios-content">
                <h1>Precios del Combustible</h1>
                <table>
                    <thead>
                        <tr>
                            <th>Tipo de Combustible</th>
                            <th>Precio por Galón</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${tablaContenido}
                    </tbody>
                </table>
            </div>
        `;
    } catch (error) {
        mainContent.innerHTML = `
            <div class="error-message">
                <p>Error cargando los precios de combustible: ${error.message}</p>
            </div>
        `;
    }
}


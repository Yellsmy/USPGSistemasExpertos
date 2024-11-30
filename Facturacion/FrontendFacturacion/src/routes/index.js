
import renderLoginView from '../views/Login/LoginView.js';
import HomeView from '../views/HomeView.js';
import { showFacturacion } from '../views/Facturacion/FacturacionView.js'; 
import { showPrecios } from '../views/Precios/PreciosView.js';

const routeChange = () => {
    const hash = window.location.hash;
    switch (hash) {
        case '#login':
            renderLoginView();
            break;
        case '#home':
            HomeView();  // Muestra la página principal
            break;
        case '#facturacion':
            showFacturacion();  // Muestra la página de facturación completa
            break;
        case '#precios':
            showPrecios();  // Muestra la página de precios
            break;
        default:
            renderLoginView();  // Muestra por defecto la vista Home si no hay hash específico
            break;
    }
};
export default routeChange;
window.addEventListener('hashchange', routeChange);
window.addEventListener('load', routeChange); 

window.addEventListener('loginSuccess', () => {
    HomeView();
});

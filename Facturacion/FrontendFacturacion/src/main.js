import { checkAuthentication, loginUser, logoutUser } from './auth/authService.js';
import routeChange from './routes/index.js';
import '../public/registerServiceWorker.js';

document.addEventListener('DOMContentLoaded', () => {
    if (!checkAuthentication()) {
        window.location.hash = '#login';
    } else {
        setupMainContent();
    }
    routeChange(); 
    window.addEventListener('hashchange', routeChange);
    
    const logoutButton = document.getElementById('logoutButton');
    if (logoutButton) {
        logoutButton.addEventListener('click', function() {
            logoutUser();
        });
    }
});

function setupMainContent() {
    document.getElementById('app').innerHTML = `
        <div class="sidebar">
        <h2 class="sidebar-header">
            <img src="./logo.jpg" alt="Logo" class="sidebar-logo">
            <span>Gasolinera</span>
        </h2>
            <a href="#home">Inicio</a>
            <a href="#facturacion">Facturación</a>
            <a href="#precios">Precios</a>
            <button id="logoutButton" class="logout-button">Cerrar Sesión</button>
        </div>
        <div id="main-content" class="content">
            <!-- Contenido principal aquí -->
        </div>
    `;
}

window.addEventListener('loginSuccess', () => {
    setupMainContent();
    window.location.hash = '#home';
});

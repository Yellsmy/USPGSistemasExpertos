
import { loginUser } from '../../auth/authService.js';
function renderLoginView() {
    const app = document.getElementById('app');
    app.innerHTML = `
        <div class="sidebar-login">
            <h2>Sistemas y Tecnologías Web</h2>
            <div class="image-container">
                <img src="./logo.jpg" alt="logo">
            </div>
            <h2>Sistema de Facturación</h2>
            <h3>Guatemala</h3>
        </div>
            
        <div class="login-container">
            <h2>Inicio de Sesión</h2>
            <form id="loginForm">
                <input type="text" id="username" placeholder="Ingrese nombre de usuario" required>
                <input type="password" id="password" placeholder="Contraseña" required>
                <button type="submit">Ingresar</button>
            </form>
            <div id="loginError" class="error-message"></div> <!-- Contenedor para mensajes de error -->
            <p>¿Has olvidado tu contraseña?</p>
        </div>
    `;

    attachLoginEvents();    
}

function attachLoginEvents() {
    const loginForm = document.getElementById('loginForm');
    loginForm.addEventListener('submit', handleLoginSubmit);
}

function handleLoginSubmit(event) {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const user = loginUser(username, password);

    if (user) {
        // Redirige al usuario o muestra contenido autenticado
        console.log('Login successful', user);
        window.location.hash = '#home'; 
        document.getElementById('loginError').textContent = ''; 
    } else {
        // Mostrar mensaje de error en la pantalla
        document.getElementById('loginError').textContent = 'Usuario o contraseña incorrectos';
        console.log('Credenciales incorrectas');
    }
}


export default renderLoginView;

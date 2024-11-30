
export default function HomeView() {
    const mainContent = document.getElementById('main-content');
    mainContent.innerHTML = `
        <div id="home-content">
            <h1>Bienvenido</h1>
            <p>Nuestro compromiso es servir a nuestros clientes</p>
            <p>25 sucursales en todo el país</p>
        </div>
    `;
}

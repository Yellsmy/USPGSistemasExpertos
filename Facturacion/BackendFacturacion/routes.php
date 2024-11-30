<?php
require_once ROOT . 'App' . DS . 'Core' . DS . 'Router.php';
$router = new Router();

$router->add('precios/mostrar', 'GET', 'TipoCombustibleController@getTiposDeCombustible');
$router->add('factura/crear', 'POST', 'FacturaController@crearFactura');
$router->add('factura/one', 'POST', 'FacturaController@obtenerFacturaPorId');
$router->add('factura/all', 'GET', 'FacturaController@obtenerTodasLasFacturas');
$router->add('factura/busqueda', 'POST', 'FacturaController@obtenerIdFacturaDetalle');

// Ruta para manejar las solicitudes OPTIONS para CORS
$router->add('factura/all', 'OPTIONS', function() {
    header("Access-Control-Allow-Origin: *");
    header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS");
    header("Access-Control-Allow-Headers: Content-Type, Authorization");
    http_response_code(204); // Responder con un estado 204 No Content
    exit;
});
$router->add('precios/mostrar', 'OPTIONS', function() {
    header("Access-Control-Allow-Origin: *");
    header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS");
    header("Access-Control-Allow-Headers: Content-Type, Authorization");
    http_response_code(204);
    exit;
});

$router->run();
?>

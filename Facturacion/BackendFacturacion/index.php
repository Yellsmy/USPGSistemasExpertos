<?php

// Define constantes para mejorar la legibilidad y evitar errores en las rutas de archivo.
define('DS', DIRECTORY_SEPARATOR);
define('ROOT', realpath(dirname(__FILE__)) . DS);

// Incluye las dependencias principales utilizando las constantes de ruta.
require_once ROOT . 'App' . DS . 'Core' . DS . 'App.php';
require_once ROOT . 'routes.php';

// Usa la clase principal de la aplicación.
use App\Core\App;

// Crear una instancia de la aplicación.
$app = new App();

// Manejo básico de errores para capturar cualquier error fatal durante la inicialización.
set_error_handler(function ($severity, $message, $file, $line) {
    throw new ErrorException($message, 0, $severity, $file, $line);
});

set_exception_handler(function ($exception) {
    echo "Uncaught exception: ", $exception->getMessage(), "\n";
});

// Opcionalmente, inicia la sesión si vas a manejar autenticaciones o datos de sesión.
//session_start();

?>


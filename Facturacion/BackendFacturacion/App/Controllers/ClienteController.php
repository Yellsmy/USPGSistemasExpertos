<?php
if (!headers_sent()) {
    header("Access-Control-Allow-Origin: *");
    header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS");
    header("Access-Control-Allow-Headers: Content-Type, Authorization");
}

if ($_SERVER['REQUEST_METHOD'] == 'OPTIONS') {
    http_response_code(204);
    exit;
}
require_once ROOT . 'App' . DS . 'Core' . DS . 'Controller.php';
require_once ROOT . 'App' . DS . 'Models' . DS . 'ClienteModel.php';

class ClienteController extends Controller {
    private $clienteModel;

    public function crearCliente($nit, $nombre) {
        $stmt = $this->pdo->prepare("CALL sp_clientes(1, NULL, ?, ?)");
        $stmt->execute([$nit, $nombre]);
        return $stmt->fetch(PDO::FETCH_ASSOC);
    }

    public function obtenerClientes() {
        $stmt = $this->pdo->prepare("CALL sp_clientes(3, NULL, NULL, NULL)");
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    public function obtenerClientePorId($id) {
        $stmt = $this->pdo->prepare("CALL sp_clientes(4, ?, NULL, NULL)");
        $stmt->execute([$id]);
        return $stmt->fetch(PDO::FETCH_ASSOC);
    }
}

?>


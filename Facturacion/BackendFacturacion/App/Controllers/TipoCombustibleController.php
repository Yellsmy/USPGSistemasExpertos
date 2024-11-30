<?php
require_once ROOT . 'App' . DS . 'Core' . DS . 'Controller.php';
require_once ROOT . 'App' . DS . 'Models' . DS . 'TipoCombustibleModel.php';

class TipoCombustibleController extends Controller {
    private $tipoCombustibleModel;

    public function __construct() {
        $this->tipoCombustibleModel = new TipoCombustibleModel();
    }

    // Obtener todos los tipos de combustible
    public function getTiposDeCombustible() {
        echo"Dentro del controller";
        try {
            $tipos = $this->tipoCombustibleModel->getAllTipos();
            $this->returnJsonResponse($tipos, 200);
        } catch (Exception $e) {
            $this->returnJsonResponse(['error' => $e->getMessage()], 500);
        }
    }

    private function returnJsonResponse($data, $statusCode) {
        header('Content-Type: application/json');
        http_response_code($statusCode);
        echo json_encode($data);
    }
}


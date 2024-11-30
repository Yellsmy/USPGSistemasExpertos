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
require_once ROOT . 'App' . DS . 'Models' . DS . 'FacturaModel.php';

class FacturaController extends Controller {
    private $facturaModel;

    public function __construct() {
        $this->facturaModel = new FacturaModel();
    }

    public function crearFactura() {
        try {
            $json = file_get_contents('php://input');
            $data = json_decode($json, true);

            if (json_last_error() !== JSON_ERROR_NONE) {
                throw new Exception('Datos JSON inválidos.');
            }

            $nit = $data['nit'] ?? 'CF';
            $tipo_combustible = $data['tipo_combustible'];
            $monto_consumo = $data['monto_consumo'];
            $forma_pago = $data['forma_pago'];
            $creado_por = 1; // Temporalmente usando 1 como el ID del creador
            //$forma_pago = "tarjeta"; // Temporalmente usando 1 como el ID de la estación
            //echo "NIT: " . $nit;
            // Consumir la API de la SAT si se proporciona un NIT
            if ($nit !== 'CF') {
                $clienteData = $this->obtenerDatosClientePorNIT($nit);
                //echo "datos: " . $clienteData;
                if (!$clienteData) {
                    throw new Exception('Error!! NIT no encontrado');
                }

                $nombreCliente = $clienteData['nombre'];
                //echo "NOMBRE DEL ARRAY: " . $nombreCliente . "\n";
            } else {
                $nombreCliente = 'Consumidor Final';
            }

            $result = $this->facturaModel->crearFactura($nit, $tipo_combustible, $monto_consumo, $forma_pago, $nombreCliente);
            $this->returnJsonResponse($result, 201);
        } catch (Exception $e) {
            $this->returnJsonResponse(['error' => $e->getMessage()], 500);
        }
    }


    private function obtenerDatosClientePorNIT($nit) {
        $NIT = "000044653948";
        $DATA1 = "SHARED_GETINFONITCOM";
        $DATA2 = "NIT|{$nit}";
        $USERNAME = "GT.000044653948.PRUEBAS33";
    
        $url = "https://felgttestaws.digifact.com.gt/gt.com.fel.api.v3/api/SHAREDINFO?NIT={$NIT}&DATA1={$DATA1}&DATA2={$DATA2}&USERNAME={$USERNAME}";
        $authorization = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IkdULjAwMDA0NDY1Mzk0OC5QUlVFQkFTMzMiLCJuYmYiOjE2OTA1NjcxNDksImV4cCI6MTcyMTY3MTE0OSwiaWF0IjoxNjkwNTY3MTQ5LCJpc3MiOiJodHRwOi8vbG9jYWxob3N0OjQ5MjIwIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo0OTIyMCJ9.LFsNNHyF1M5CTO50QYbBQuJbXVg_G29EbRo0juAY7oM';
    
        //echo "URL: " . $url . "\n";
    
        $headers = array();
        $headers[] = 'Content-type: Application/json';
        $headers[] = 'Authorization: ' . $authorization;
    
        $ch = curl_init();
    
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    
        // Deshabilitar la verificación SSL para pruebas (no recomendado para producción)
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
        curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
    
        $response = curl_exec($ch);
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        $curlError = curl_error($ch);
    
        // Imprimir el código de respuesta HTTP
        //echo "Código de respuesta HTTP: " . $httpCode . "\n";
        // Imprimir la respuesta de la API
        //echo "Respuesta de la API:\n";
        //echo "<pre>";
        // var_dump($response);
        // echo "</pre>";
    
        // Imprimir errores de cURL
        if ($response === false) {
            echo "Error de cURL: " . $curlError . "\n";
        }
    
        curl_close($ch);
    
        if ($httpCode === 200) {
            $data = json_decode($response, true);
            if (json_last_error() === JSON_ERROR_NONE && isset($data['RESPONSE'][0])) {
                $responseItem = $data['RESPONSE'][0];
                $nombreCliente = str_replace(['Ñ', ','], ['N', ' '], $responseItem['NOMBRE']);
                $nombreCliente = preg_replace('/[^A-Za-z0-9 ]/', '', $nombreCliente);
                //echo "NOMBRE RESPUESTA:" . $nombreCliente . "\n";
                return [
                    'nombre' => $nombreCliente,
                    
                    'nit' => $responseItem['NIT']
                ];
            } else {
                echo "Error de JSON: " . json_last_error_msg() . "\n";
            }
        } else {
            echo "Error en la solicitud: Código HTTP " . $httpCode . "\n";
        }
    
        return null;
    }

    public function obtenerFacturaPorId() {
        try {
            $json = file_get_contents('php://input');
            $data = json_decode($json, true);
    
            if (json_last_error() !== JSON_ERROR_NONE) {
                throw new Exception('Datos JSON inválidos.');
            }
    
            if (!isset($data['id_factura_detalle'])) {
                throw new Exception('ID de factura no proporcionado.');
            }
    
            $id_factura_detalle = intval($data['id_factura_detalle']);
            $factura = $this->facturaModel->obtenerUnaFactura($id_factura_detalle);
    
            if (!$factura) {
                throw new Exception('Factura no encontrada.');
            }
    
            $this->returnJsonResponse($factura, 200);
        } catch (Exception $e) {
            $this->returnJsonResponse(['error' => $e->getMessage()], 500);
        
        }
    }

    public function obtenerTodasLasFacturas() {
        try {
            $facturas = $this->facturaModel->getAllFacturas();
            if (!$facturas) {
                throw new Exception('No se encontraron facturas.');
            }
            $this->returnJsonResponse($facturas, 200);
        } catch (Exception $e) {
            $this->returnJsonResponse(['error' => $e->getMessage()], 500);
        }
    }
    
    public function obtenerIdFacturaDetalle() {
        try {
            $json = file_get_contents('php://input');
            $data = json_decode($json, true);
            //echo "Número factura" . $data['numero_factura'] . "\n"; 
            if (json_last_error() !== JSON_ERROR_NONE) {
                throw new Exception('Datos JSON inválidos.');
            }
    
            if (!isset($data['numero_factura'])) {
                throw new Exception('Número de factura no proporcionado.');
            }
    
            $numero_factura = $data['numero_factura'];
            $id_factura_detalle = $this->facturaModel->busquedaPorNumero($numero_factura);
    
            if (!$id_factura_detalle) {
                throw new Exception('Factura no encontrada.');
            }
    
            $this->returnJsonResponse($id_factura_detalle, 200);
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
?>



<?php

require_once ROOT . 'App' . DS . 'Core' . DS . 'Database.php';

class FacturaModel {
    protected $pdo;

    public function __construct() {
        $this->pdo = Database::getInstance()->getConnection();
    }

    public function crearFactura($nit, $tipo_combustible, $monto_consumo, $forma_pago, $nombreCliente) {
        // echo "NIT---:" . $nit . "\n";
        // echo "TIPO---:" . $tipo_combustible . "\n";
        // echo "MONTO---:" . $monto_consumo . "\n";
        // echo "FORMA DE PAGO---:" . $forma_pago . "\n";
        // echo "NOMBRE---:" . $nombreCliente . "\n";
        // Configuraciones iniciales
        $parametroOpcion = 1;
        $parametroEstacion = 1;
        $parametroUsuario = 1;
        $parametroVacio = null;

        // Iniciar transacción
        $this->pdo->beginTransaction();
        try {
            // Insertar o actualizar cliente
            $stmtCliente = $this->pdo->prepare("CALL sp_clientes(?, ?, ?, ?, ?)");
            $stmtCliente->bindParam(1, $parametroOpcion, PDO::PARAM_INT);
            $stmtCliente->bindParam(2, $parametroVacio, PDO::PARAM_INT);
            $stmtCliente->bindParam(3, $nit, PDO::PARAM_STR);
            $stmtCliente->bindParam(4, $nombreCliente, PDO::PARAM_STR);
            $stmtCliente->bindParam(5, $parametroUsuario, PDO::PARAM_INT);
            $stmtCliente->execute();
            $resultCliente = $stmtCliente->fetch(PDO::FETCH_ASSOC);
            $idCliente = $resultCliente['v_idCliente'];
            $stmtCliente->closeCursor();

            if (!$idCliente) {
                throw new Exception("No se pudo insertar al cliente en la base de datos.");
            }

            // Crear encabezado de factura
            $numero_factura = uniqid(); // Genera un número de factura único
            $serie = 'A'; // Puedes ajustar esto según tus necesidades
            //echo "ENTRÓ AQUÍ" . $idCliente . "\n";
            $stmtEncabezado = $this->pdo->prepare("CALL sp_factura_encabezado(?, ?, ?, ?, ?, ?, ?, ?)");
            $stmtEncabezado->bindParam(1, $parametroOpcion, PDO::PARAM_INT);
            $stmtEncabezado->bindParam(2, $parametroVacio, PDO::PARAM_INT);
            $stmtEncabezado->bindParam(3, $parametroEstacion, PDO::PARAM_INT);
            $stmtEncabezado->bindParam(4, $numero_factura, PDO::PARAM_STR);
            $stmtEncabezado->bindParam(5, $serie, PDO::PARAM_STR);
            $stmtEncabezado->bindParam(6, $idCliente, PDO::PARAM_INT);
            $stmtEncabezado->bindParam(7, $forma_pago, PDO::PARAM_STR);
            $stmtEncabezado->bindParam(8, $parametroUsuario, PDO::PARAM_INT);
            $stmtEncabezado->execute();
            $resultEncabezado = $stmtEncabezado->fetch(PDO::FETCH_ASSOC);
            $idFacturaEncabezado = $resultEncabezado['v_id_factura_encabezado'];
            //echo "ENTRÓ AL DETALLE FACTURA" . $idFacturaEncabezado . "\n";
            $stmtEncabezado->closeCursor();

            if (!$idFacturaEncabezado) {
                throw new Exception("No se pudo crear el encabezado de la factura.");
            }

            // Crear detalle de factura
            //echo "ENTRÓ AL DETALLE FACTURA" . $idFacturaEncabezado . "\n";
            $stmtDetalle = $this->pdo->prepare("CALL sp_factura_detalle(?, ?, ?, ?, ?, ?)");
            $stmtDetalle->bindParam(1, $parametroOpcion, PDO::PARAM_INT);
            $stmtDetalle->bindParam(2, $parametroVacio, PDO::PARAM_INT);
            $stmtDetalle->bindParam(3, $idFacturaEncabezado, PDO::PARAM_INT);
            $stmtDetalle->bindParam(4, $tipo_combustible, PDO::PARAM_STR);
            $stmtDetalle->bindParam(5, $monto_consumo, PDO::PARAM_STR);
            $stmtDetalle->bindParam(6, $parametroUsuario, PDO::PARAM_INT);
            $stmtDetalle->execute();
            $resultDetalle = $stmtDetalle->fetch(PDO::FETCH_ASSOC);
            $idFacturaDetalle = $resultDetalle['v_id_factura_detalle'];
            $stmtDetalle->closeCursor();

            if (!$idFacturaDetalle) {
                throw new Exception("No se pudo crear el detalle de la factura.");
            }

            // Confirmar transacción
            $this->pdo->commit();
            return $idFacturaDetalle;
        } catch (Exception $e) {
            $this->pdo->rollBack();
            throw $e;  // Propagar la excepción para manejo externo
        }
    }

    public function obtenerUnaFactura($id_factura_detalle) {
        $stmt = $this->pdo->prepare("CALL sp_factura_detalle(5, ?, NULL, NULL, NULL, NULL)");
        $stmt->bindParam(1, $id_factura_detalle, PDO::PARAM_INT);
        $stmt->execute();
        $factura = $stmt->fetch(PDO::FETCH_ASSOC);
        $stmt->closeCursor();
        return $factura;
    }

    public function getAllFacturas() {
        $stmt = $this->pdo->prepare("CALL sp_factura_detalle(4, NULL, NULL, NULL, NULL, NULL)");
        $stmt->execute();
        $facturas = $stmt->fetchAll(PDO::FETCH_ASSOC);
        $stmt->closeCursor();
        return $facturas;
    }

    public function busquedaPorNumero($numero_factura) {
        //echo "Número factura" . $numero_factura . "\n"; 
        $stmt = $this->pdo->prepare("CALL sp_factura_encabezado(3, NULL, NULL, ?, NULL, NULL, NULL, NULL)");
        $stmt->bindParam(1, $numero_factura, PDO::PARAM_STR);
        $stmt->execute();
        $id_factura_detalle = $stmt->fetchAll(PDO::FETCH_ASSOC);
        $stmt->closeCursor();
        return $id_factura_detalle;
    }
    
    
}
?>

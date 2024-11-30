<?php

require_once ROOT . 'App' . DS . 'Core' . DS . 'Database.php';

class ClienteModel {
    protected $pdo;

    public function __construct() {
        $this->pdo = Database::getInstance()->getConnection();
    }

    public function guardarCliente($nombre, $nit, $ubicacion) {
        $sql = "INSERT INTO clientes (nombre, nit, ubicacion) VALUES (?, ?, ?)";
        $stmt = $this->pdo->prepare($sql);
        $stmt->execute([$nombre, $nit, $ubicacion]);
        return $this->pdo->lastInsertId();
    }

    public function obtenerClientePorNIT($nit) {
        $sql = "SELECT * FROM clientes WHERE nit = ?";
        $stmt = $this->pdo->prepare($sql);
        $stmt->execute([$nit]);
        return $stmt->fetch(PDO::FETCH_ASSOC);
    }
}

?>

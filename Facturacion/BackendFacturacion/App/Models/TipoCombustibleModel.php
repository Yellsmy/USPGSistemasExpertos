<?php

require_once ROOT . 'App' . DS . 'Core' . DS . 'Database.php';

class TipoCombustibleModel {
    protected $pdo;

    public function __construct() {
        $this->pdo = Database::getInstance()->getConnection();
    }

    // Obtener todos los tipos de combustible usando procedimiento almacenado
    public function getAllTipos() {
        $stmt = $this->pdo->prepare("CALL sp_tipoCombustible(4, NULL, NULL, NULL, NULL)");
        $stmt->execute();
        $tiposCombustible = $stmt->fetchAll(PDO::FETCH_ASSOC);
        $stmt->closeCursor();
        return $tiposCombustible;
    }
}

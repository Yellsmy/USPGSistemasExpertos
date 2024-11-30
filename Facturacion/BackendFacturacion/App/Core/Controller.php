<?php

class Controller {
    /**
     * Carga el modelo especificado.
     * 
     * @param string $model Nombre del modelo a cargar.
     * @return object Instancia del modelo.
     */
    public function model($model) {
        $modelPath = ROOT . 'App' . DS . 'Models' . DS . $model . '.php';
        if (file_exists($modelPath)) {
            require_once $modelPath;
            return new $model();
        } else {
            // Maneja el error, por ejemplo, lanzando una excepción o registrando un error.
            throw new Exception("El modelo solicitado no existe: " . $model);
        }
    }

    // Temporalmente deshabilitado ya que no se están utilizando vistas en el backend.
    /*
    public function view($view, $data = []) {
        $viewPath = ROOT . 'App' . DS . 'Views' . DS . $view . '.php';
        if (file_exists($viewPath)) {
            extract($data);
            require_once $viewPath;
        } else {
            // Maneja el error, por ejemplo, lanzando una excepción o registrando un error.
            throw new Exception("La vista solicitada no existe: " . $view);
        }
    }
    */
}

?>

<?php

class Router {
    private $routes = [];

    public function add($uri, $method, $callback) {
        $this->routes[] = ['uri' => $uri, 'method' => $method, 'callback' => $callback];
    }
 
    public function run() {
        $uri = $this->getCurrentUri();
        $requestMethod = $_SERVER['REQUEST_METHOD'];
    
        foreach ($this->routes as $route) {
            if ($this->uriMatch($route['uri'], $uri) && $route['method'] === $requestMethod) {
                $this->executeCallback($route['callback']);
                return;
            }
        }
    
        $this->sendNotFound();
    }

    private function getCurrentUri() {
        $uri = $_SERVER['REQUEST_URI'];
        $scriptDir = dirname($_SERVER['SCRIPT_NAME']); 
        return trim(str_replace($scriptDir, '', $uri), '/');
    }

    private function uriMatch($routeUri, $currentUri) {
        return $routeUri === $currentUri;
    }

    private function executeCallback($callback) {
        if (is_callable($callback)) {
            call_user_func($callback);
        } else if (is_string($callback)) {
            $this->callControllerAction($callback);
        }
    }

    private function callControllerAction($callback) {
        list($class, $method) = explode('@', $callback);
        require_once ROOT . 'App' . DS . 'Controllers' . DS . "{$class}.php";
        $controller = new $class();
        call_user_func_array([$controller, $method], []);
    }    

    private function sendNotFound() {
        header("HTTP/1.0 404 Not Found");
        echo '404 Not Found';
    }
}
?>

<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: GET, POST, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type, Authorization");

ini_set('display_errors', 1);
error_reporting(E_ALL);
header("Content-Type: application/json; charset=utf-8");

$host = 'db';
$user = 'root';
$password = 'root';
$database = 'gestor_db';

$conexion = new mysqli($host, $user, $password, $database);
if ($conexion->connect_error) {
    die(json_encode(["error" => "Conexión fallida: " . $conexion->connect_error]));
}

$conexion->set_charset("utf8");

$sql = "SELECT * FROM agendar";
$resultado = $conexion->query($sql);
if (!$resultado) {
    die(json_encode(["error" => "Consulta fallida: " . $conexion->error]));
}

$data = [];
while ($fila = $resultado->fetch_assoc()) {
    $data[] = $fila;
}

echo json_encode($data);
$conexion->close();
?>

<?php
$servername = "localhost";
$username = "username";
$password = "password";

// Create connection
$conn = new mysqli.connect($servername, $username, $password);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";
?>
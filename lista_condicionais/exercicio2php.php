<?php
echo "Este programa identifica se o número é positivo ou negativo";
$numero = floatval(readline("Digite um número: "));

if ($numero > 0) {
    echo "O número é POSITIVO!";
} elseif ($numero < 0) {
    echo "O número é NEGATIVO!";
} else {
    echo "O número é ZERO";
}
?>
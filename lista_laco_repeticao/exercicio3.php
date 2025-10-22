<?php

echo "Este programa exibe uma tabuada deste número\n";
$numero = (int)readline("Digite um número inteiro positivio: ");
$tabuada = 0;

for ($i = 0; $i < 10; $i++) {
    $multiplicador = $i + 1; 
    $resultado = $numero * $multiplicador;
    echo "$numero x $multiplicador = $resultado\n";
}

?>
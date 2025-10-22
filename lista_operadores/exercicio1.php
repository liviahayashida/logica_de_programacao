<?php
echo "Este programa mostra a soma, subtração, multiplicação, divisão, resto da divisão e potenciação entre dois números\n";
$number1 = (float)readline("Digite seu primeiro número: ");
$number2 = (float)readline("Digite seu segundo número: ");

$soma = $number1 + $number2;
$subtracao = $number1 - $number2;
$multiplicacao = $number1 * $number2;

if ($number2 == 0) {
    $divisao = "Não é possível dividir por zero";
    $restodivisao = "Não é possível calcular o resto com zero";
} else {
    $divisao = $number1 / $number2;
    $restodivisao = $number1 % $number2;
}

$potenciacao = pow($number1, $number2);
echo "Seus resultados são: \n";
echo "soma: $soma; \n";
echo "subtração: $subtracao; \n";
echo "multiplicação: $multiplicacao; \n";
echo "divisão: $divisao; \n";
echo "resto da divisão: $restodivisao; \n";
echo "potenciação: $potenciacao\n";

?>
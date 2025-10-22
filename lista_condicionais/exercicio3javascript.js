console.log("Este programa indica o maior entre dois números");
let numero1 = parseFloat(prompt("Digite o primeiro número: "));
let numero2 = parseFloat(prompt("Digite o segundo número: "));

let resultado;
if (numero1 > numero2) {
    resultado = `O maior número é: ${numero1}`;
} else if (numero2 > numero1) {
    resultado = `O maior número é: ${numero2}`;
} else {
    resultado = `Os números são iguais: ${numero1}`;
}
console.log(resultado);
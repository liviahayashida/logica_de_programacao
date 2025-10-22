console.log("Este programa realiza operações em sequencia");
let numero = 10;

let soma = numero + 5;
let multiplicacao = soma * 2;
let subtracao = multiplicacao - 8;
let divisao = subtracao / 3;
let resto = divisao % 4;
let potencia = resto ** 2;

console.log(`Após += 5: ${soma}`);
console.log(`Após *= 2: ${multiplicacao}`);
console.log(`Após -= 8: ${subtracao}`);
console.log(`Após /= 3: ${divisao}`);
console.log(`Após %= 4: ${resto}`);
console.log(`Após **= 2: ${potencia}`);
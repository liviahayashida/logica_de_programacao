#include <iostream>

int main() {
    std::cout << "Este programa calcula a soma de todos os números pares entre 1 e o numero escolhido" << std::endl;
    int numero;
    std::cout << "Digite um número inteiro positivo: ";
    std::cin >> numero;
    int soma_atual = 0;
    for (int i = 0; i <= numero; i += 2) {
        soma_atual += i;
    }
    std::cout << "A soma dos números pares é: " << soma_atual << std::endl;
    return 0;
}
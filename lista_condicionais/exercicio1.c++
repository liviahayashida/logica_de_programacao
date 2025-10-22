#include <iostream>
#include <cmath> //para matematica

int main() {
    std::cout << "Este programa verifica se o numero é impar ou par" << std::endl;

    std::cout << "Digite um número: ";
    std::cin >> numero;

    int numero_inteiro = static_cast<int>(numero);
    if (numero_inteiro % 2 == 0) {
        std::cout << "Número é PAR!" << std::endl;
    } else {
        std::cout << "Número é ÍMPAR!" << std::endl;
    }
    return 0;
}
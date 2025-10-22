#include <iostream>
#include <cmath>

int main() {
    std::cout << "Este programa calcula o resto da divisao por diversos numeros" << std::endl;

    float number_float;
    std::cout << "Digite um numero: ";
    if (!(std::cin >> number_float)) {
        std::cerr << "Entrada inválida. Por favor, digite um número." << std::endl;
        return 1;
    }
    int number = static_cast<int>(number_float);

    int restodivisaopor2 = number % 2;
    int restodivisaopor3 = number % 3;
    int restodivisaopor5 = number % 5;
    int restodivisaopor10 = number % 10;

    if (restodivisaopor2 == 0) {
        std::cout << "Numero PAR!\n";
    } else {
        std::cout << "Numero IMPAR!\n";
    }
    std::cout << "Resto da divisao por 2: " << restodivisaopor2 << std::endl;
    std::cout << "Resto da divisao por 3: " << restodivisaopor3 << std::endl;
    std::cout << "Resto da divisao por 5: " << restodivisaopor5 << std::endl;
    std::cout << "Resto da divisao por 10: " << restodivisaopor10 << std::endl;

    return 0;
}
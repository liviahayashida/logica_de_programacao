print("Este programa mostra a soma, subtração, multiplicação, divisão, resto da divisão e potenciação entre dois números")
number1 = float(input("Digite seu primeiro número: "))
number2 = float(input("Digite seu segundo número: "))

soma = number1+number2
subtracao = number1 - number2
multiplicacao = number1*number2
divisao = number1/number2
restodivisao = number1% number2
potenciacao = number1**number2

print(f"Seu resultados são: soma: {soma}; \nsubtração: {subtracao}; \nmultiplicação: {multiplicacao}; \ndivisão: {divisao}; \nresto da divisão: {restodivisao}; \npotenciação:{potenciacao}")

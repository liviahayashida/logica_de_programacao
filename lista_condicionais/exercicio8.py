print("Este programa é uma calculadora simples com condicionais")
numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite um número: "))
operador = input("Digite um operador (+,-,*,/): ")

if (operador=="+"):
    print(f"O resultado da soma é {numero1+numero2}!")
elif (operador=="-"):
    print(f"O resultado da subtração é {numero1-numero2}!")
elif (operador=="*"):
    print(f"O resultado da multiplicação é {numero1*numero2}!")
else:
    print(f"O resultado da divisão é {numero1/numero2}!")
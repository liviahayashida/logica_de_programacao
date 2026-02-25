print("Este programa apresenta uma calculadora simples")
num1 = float(input("Digite seu primeiro número: "))
num2 = float(input("Digite seu segundo número: "))
operacao = input("Digite + para somar, - para subtrair, * para multiplicar e / para dividir: ")
if operacao=="+":
    print(f"A soma de {num1} mais {num2} é {num1+num2:.1f}")
elif operacao=="-":
    print(f"A subtração de {num1} menos {num2} resulta em {num1-num2:.1f}")
elif operacao=="*":
    print(f"A multiplicação de {num1} vezes {num2} é igual a {num1*num2:.1f}")
elif operacao=="/":
    print(f"A divisão de {num1} por {num2} resulta em {num1/num2:.1f}")
else:
    print("Digite uma operação elegivél!")
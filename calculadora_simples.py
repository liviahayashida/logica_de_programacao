print('Este programa simula uma calculadora simples:')
escolha = input("Digite... \n+ para somar; \n- para subtrair; \n* para multiplicar; \n/ para dividir; \n ")
num1 = float(input("Digite seu primeiro número: "))
num2 = float(input("Digite o segundo número: "))
match escolha:
    case "+":
        print(f"a soma de {num1} mais {num2} é igual a {num1+num2}")
    case "-":
        print(f"A subtração de {num1} menos {num2} é igual a {num1-num2}")
    case "*":
        print(f"A multiplicação de {num1} com {num2} é igual a {num1*num2}")
    case '/':
        print(f"A divisão de {num1} por {num2} é igual a {num1/num2}")       

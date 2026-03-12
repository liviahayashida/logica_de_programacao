print("Este programa calcula a area de um quadrado, retangulo ou triangulo em cm")
escolha = int(input("Digite o número da opção escolhida: \n1. área do quadrado; \n2. área do retangulo; \n3. área do triangulo: \n"))

match escolha:
    case 1:
        lado = float(input("Digite o comprimento lateral do quadrado: "))
        print(f"A área do quadrado é igual a {lado**2:.2f}")
    case 2:
        base = float(input("Digite o comprimento da base: "))
        altura = float(input("Digite a altura do retangulo: "))
        print(f"A área do retangulo é igual a {base*altura}")
    case 3:
        base = float(input("Digite o comprimento da base: "))
        altura = float(input("Digite a altura do triangulo: "))
        print(f"A área do triangulo é igual a {(base*altura)/2}")
    
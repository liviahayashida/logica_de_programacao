print('Este programa traduz as cores de portugues para o ingles')
escolha = int(input("Digite o número equivalente a opção desejada: \n1. vermelho; \n2. azul; \n3. verde; \n4. amarelo; \n"))

match escolha:
    case 1:
        print("vermelho é red")
    case 2:
        print("azul é blue")
    case 3:
        print("verde é green")
    case 4:
        print("amarelo é yellow")
        
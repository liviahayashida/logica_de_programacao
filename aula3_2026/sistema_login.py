print("Este programa simula um sistema simples de login")
login = int(input("Digiteo numero da opção escolhida: \n1. Admin; \n2. professor; \n3. Aluno; \n"))
usuario = input("Digite seu usuário: ")

match login:
    case 1:
        print("Voce entrou como Administrador!")
    case 2:
        print("Voce entrou como professor!")
    case 3:
        print("Voce entrou como aluno!")
print("Este programa verifica seu login")
usuario = (input("Digite seu usuário: "))
senha = int(input("Digite sua senha: "))

if (usuario == "admin" and senha== 1234):
    print("ACESSO PERMITIDO!")
else:
    print("Acesso negado...tente novamente!")
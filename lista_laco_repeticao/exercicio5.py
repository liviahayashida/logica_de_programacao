print("Este programa solicita uma senha até que o usuário acerte")
senha = input("Digite sua senha: ")

senha_correta = "python123"
senha_digitada = ""

while senha_digitada != senha_correta:
    print("Senha incorreta!!! Tente novamente")
    senha_digitada = input("Digite sua senha: ")
print("Acesso permitido!🎉🎉🎉")

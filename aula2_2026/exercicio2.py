print("Este programa solicita a idade do usuário e informa se ele é menor de idade, maior de idade ou idoso")
idade = int(input("Digite sua idade: "))
if idade<18:
    print("Voce é menor de idade")
elif idade>=18 and idade<65:
    print("Voce é maior de idade")
else:
    print("Voce é idoso :)")
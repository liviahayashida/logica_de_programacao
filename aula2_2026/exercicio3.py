print("Este programa te classifica como criança, adolescente, adulto ou idoso de acordo com a sua idade")
idade = int(input("Digite sua idade: "))
if idade<=12:
    print("Voce é criança!")
elif idade>12 and idade<18:
    print("Voce é adolescente!")
elif idade>=18 and idade<=64:
    print("Voce é adulto")
else:
    print("Voce é idoso!")
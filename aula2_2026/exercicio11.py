print("Este programa mostra qual sua classificação no time de futebol")
idade = int(input("Digite sua idade: "))
if idade<18:
    print("Voce é um jogador juvenil")
elif idade<36:
    print("Voce é um jogador adulto")
else:
    print("Voce é um jogador veterano")
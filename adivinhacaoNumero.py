import random
print("Este programa escolhe um numero aleatorio de 1 a 10 e permite que voce tente adivinhar em até 3 tentativas")
numero = random.randint(1, 10)
for i in range (3):
    adivinhar = int(input("Faça seu chute (de 1 a 10): "))
    if adivinhar==numero:
        print("Parabenssss, voce acertou!!!")
    else:
        print("Vamos tentar de novo...")
print(f"O numero sorteado dessa rodada era {numero}")

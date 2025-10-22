print("Este programa é um jogo de adivinhação")
import random
numero = random.randint(1, 50)
palpite = 0

print("Tente adivinhar o número entre 1 e 50!")
while palpite != numero:
    palpite = int(input("Digite seu palpite: "))
    if palpite > numero:
        print("Muito alto! Tente novamente.")
    elif palpite < numero:
        print("Muito baixo! Tente novamente.")
print("Parabéns! Você acertou!")
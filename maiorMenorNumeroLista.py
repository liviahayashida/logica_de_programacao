print("Este programa mostra, dentre 5 digitos, o maior e o menor deles")
maior = 0
menor = 0
for i in range (5):
    numero = int(input(f"Digite seu {i+1} numero: :)"))
    if i == 0:
        maior = numero
        menor = numero
    elif numero > maior:
            maior = numero
    elif numero < menor:
            menor = numero
print(f"Seu maior numero é: {maior}")
print(f"Seu menor numero é: {menor}")
print("Este programa verifica se um numero é primo ou nao")
numero = int(input("Digite um numero: "))
contador = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        contador += 1
if contador == 2:
    print("É primo")
else:
    print("Nao é primo")

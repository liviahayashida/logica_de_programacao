print("Este programa faz calculos com 6 numeros reais")
numeros = []
maior=0
menor=0
for i in range(0,6):
    num = int(input(f"Digite seu numero {i+1}: "))
    numeros.append(num)
    maior = max(numeros)
    menor = min(numeros)

soma = sum(numeros)
print(f"Soma: {soma}")
print(f"media: {soma/6}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")

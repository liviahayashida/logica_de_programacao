print("Este programa inverte a lista")
numeros = []

for i in range(0, 10):
    num = int(input(f"Digite seu numero {i+1} inteiro: "))
    numeros.append(num)

print(f"Lista original: {numeros}")
lista_invertida = numeros[::-1]

print(f"Lista invertida: {lista_invertida}")
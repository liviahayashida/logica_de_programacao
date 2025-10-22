print("Este programa separa pares de impares")
numeros = []
pares = []
impares = []

for i in range(0,10):
    num = int(input(f"Digite seu numero {i+1} inteiro: "))
    numeros.append(num)
    if num%2 ==0:
        pares.append(num)
    else:
        impares.append(num)

print(f"Todos os numeros: {numeros}")
print(f"Numeros pares: {pares}")
print(f"Numeros impares: {impares}")

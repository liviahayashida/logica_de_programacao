print("Este programa cria uma lista com 10 numeros e mostra apenas os numeros pares")
numeros = []
pares = []
for i in range(10):
    num = int(input(f"Digite seu {i+1} numero:"))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)

print(f"Os numeros digitados foram: {numeros}")
print(f"Os numeros pares digitados foram: {pares}")

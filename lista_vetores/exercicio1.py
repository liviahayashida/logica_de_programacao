print("Este programa le 5 numeros de uma lista")
numeros = []
for i in range(0,5):
    num = int(input(f"Digite seu numero {i+1}: "))
    numeros.append(num)

print(f"Números Digitados: {numeros}")
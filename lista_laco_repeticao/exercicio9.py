print("Este programa exibe a contagem de números pares, ímpares e a soma total.")
numeros = []
pares = 0
impares = 0
soma_total = 0

for i in range(0, 10):
    nota = int(input(f"Digite o {i+1}º número: "))
    numeros.append(nota)
    soma_total = soma_total+nota

    if nota % 2 == 0:
        pares = pares+1
    else:
        impares = impares+1
        
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")
print(f"Soma total: {soma_total}")
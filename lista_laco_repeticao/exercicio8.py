print("Este programa mostra o maior e menor número enviados")
numeros = []
maior=0
menor=0
for i in range(0,5):
    nota = int(input(f"Digite seu numero {i+1}: "))
    numeros.append(nota)
    maior = max(numeros)
    menor = min(numeros)

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
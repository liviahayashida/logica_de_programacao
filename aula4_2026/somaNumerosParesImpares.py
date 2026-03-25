print("Este programa soma os pares e os impares de 1 até o número selecionado")
num = int(input("Digite um numero: "))
pares = 0
impares = 0
for i in range(1, numero + 1):
    if i % 2 == 0:
        pares += i
    else:
        impares += i
print("Soma dos pares:", pares)
print("Soma dos ímpares:", impares)

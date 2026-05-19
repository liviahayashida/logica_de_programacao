print("Este programa cria uma lista com 5 numeros inteiros e exibe cada um ao quadrado")

numeros = []
for i in range(5):
    num = int(input(f"Digite seu {i+1} numero: "))
    num = num ** 2
    numeros.append(num)

print(f"Os numeros ao quadrado são: {numeros}")
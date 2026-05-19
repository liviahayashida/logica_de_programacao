print("Este programa conta quantas vezes o numero 3 aparece em uma lista")
print("Digite 'p' para parar de digitar\n")

numeros = []
contador = 0
entrada = input("Digite um numero: ")

while entrada.lower() != "p":
    num = int(entrada)
    numeros.append(num)
    if num == 3:
        contador = contador + 1
    entrada = input("Digite um numero: ")

print(f"O numero 3 aparece {contador} vezes nas lista de numeros digitados \n {numeros}")
print("Este programa conta quantos valores positivos, negativos e zeros foram digitados")

positivos = 0
negativos = 0
zeros = 0
resposta = "c"

while resposta != "s" and resposta != "S":
    num = int(input("Digite um numero: "))

    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        zeros += 1

    resposta = input("Digite c para continuar e s para sair: ")

print("Positivos:", positivos)
print("Negativos:", negativos)
print("Zeros:", zeros)
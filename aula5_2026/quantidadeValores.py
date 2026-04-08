print("Este programa conta quantos valores positivos, negativos e zeros foram digitados")
positivos = 0
negativos = 0
zeros = 0
num = int(input("Digite um numero: "))
resposta = "c"

def seletiva(num):
    if num > 0:
        return positivos = positivos+1
    elif num <0:
        return negativos = negativos+1
    elif num == 0:
        return zeros = zeros+1
     

while resposta != "s" or resposta != "S":
    num = int(input("Digite seu numero: "))
    resposta = input("Digite c para continuar e s para sair: ")
    def seletiva(num)
    
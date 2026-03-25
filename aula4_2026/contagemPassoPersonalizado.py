print("Este programa pede tres números: início, fim e passo")
inicio = int(input("Digite o numero de inicio: "))
fim = int(input("Digite o numero final: "))
passo = int(input("Digite um numero para o passo: "))
for i in range(inicio, fim, passo):
    print(i)
    
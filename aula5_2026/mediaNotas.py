print("Este programa calcula a média de suas notas")

nota = 0
soma = 0
quantidade = 0 
while nota >=0:
    nota = int(input("Digite sua nota: "))
    if nota>=0:
        soma = soma+nota
        quantidade= quantidade+1
        print(f"Sua media atual é de: {soma/quantidade}")

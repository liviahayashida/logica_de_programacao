print("Este programa solicita 5 notas de calcula a média")
soma = 0
for i in range (5):
    nota = float(input("Digite sua nota: "))
    soma+=nota
print(f" A sua média é de {soma/5}")
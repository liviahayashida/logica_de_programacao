print("Este programa calcula a média de quantas notas você quiser")
quantasnotas = int(input("Digite o número de notas que deseja usar na média: "))
soma = 0
for i in range(quantasnotas):
    nota = int(input(f"Digite a nota: "))
    soma += nota
media = soma / quantasnotas
print(f"Média: {media}")
if media >= 7:
    print("Aprovado!!!")
elif media >= 5:
    print("Recuperação!")
else:
    print("Reprovado :(")
print("Este programa calcula a média e situação do aluno")
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = (nota1+nota2) /2

if (media>=7):
     print ("Aprovado")
elif(media>=5 and media<7):
     print("Recuperação")
else:
     print("Reprovado")
print("Este sistema classifica a nota de um aluno: ")
nota = int(input("Digite sua nota: "))
if nota==100 or nota>=90:
    print("Voce tirou A!")
elif nota<90 and nota>=80:
    print("Voce tirou B!")
elif nota<80 and nota>=70:
    print("Voce tirou C!")
elif nota<70 and nota>=60:
    print("Voce tirou D!")
else:
    print("Voce tirou F!")
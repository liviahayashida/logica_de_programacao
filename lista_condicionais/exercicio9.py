print("Este programa categoriza voce pela sua idade")
idade = int(input("Digite sua idade: "))

if (idade<12):
     print ("Voce é criança!")
elif(idade>=12 and idade<=17):
     print("Voce é Adolescente!")
elif(idade>=18 and idade<=59):
    print("Voce é Adulto!")
else:
     print("Voce é Idoso")
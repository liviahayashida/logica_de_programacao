print("Este programa calcula o IMC e te classifica")
peso = (float(input("Digite seu peso: ")))
altura = float(input("Digite sua altura: (exemplo: 1.50, digite em metros)"))
imc= (altura*altura)/peso
if imc<18.5:
    print("Voce esta abaixo do peso")
elif imc>=18.5 and imc<=24.9:
    print("Voce esta com peso normal")
elif imc>=25.0 and imc<=29.9:
    print("Voce esta com sobrepeso")
elif imc>=30.0 and imc<=39.9:
    print("Voce esta com obesidade")
else:
    print("Voce esta com sobrepeso grave")
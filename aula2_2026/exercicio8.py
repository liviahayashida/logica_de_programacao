print("Este programa calcula o IMC e te classifica")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura (exemplo: 1.50, digite em metros): "))
imc = peso / (altura ** 2)
print(f"Seu IMC é {imc:.2f}")
if imc < 18.5:
    print("Você está abaixo do peso")
elif imc <= 24.9:
    print("Você está com peso normal")
elif imc <= 29.9:
    print("Você está com sobrepeso")
elif imc <= 39.9:
    print("Você está com obesidade")
else:
    print("Você está com obesidade grave")
print("Este programa calcula o imc de uma pessoa")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura (ex: 1.70):"))
print(f"Seu IMC é: {peso/(altura**2):.2f}")
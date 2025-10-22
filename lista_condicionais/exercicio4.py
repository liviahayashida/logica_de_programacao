print("Este programa identifica o maior entre tres números")
numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite um número: "))
numero3 = float(input("Digite um número: "))

if (numero1>numero2 and numero1>numero3):
     print (f"O maior número é: {numero1}")
elif(numero1<numero2 and numero3<numero2):
     print(f"O maior número é: {numero2}")
else:
     print(f"O maior número é: {numero3}")
print("Este programa exibe 5 numeros ao quadrado")

numeros = []
contador = 0
for i in range (5):
    numero = int(input(f"Digite seu {i+1} número: "))
    numeros.append(numero*numero)
print("Seus numeros ao quadrado: ")
for resultado in numeros:
    print(resultado)
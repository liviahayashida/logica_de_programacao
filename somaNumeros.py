print("Este programa exibe a soma de 1 até esse número.")
num = int(input("Digite um número: "))
soma = 0
for i in range (1, num, +1):
    soma = soma + i
print(f"A soma é igual a {soma}")
print("Este programa calcula a soma de todos os números pares entre 1 e o numero escolhido")
numero = int(input("Digite um número inteiro positivio: "))
soma_atual = 0

for i in range (0, numero, 2): #,2 para ir de 2 em 2
    soma_atual+=i
print(f"A soma dos números pares é: {soma_atual}")
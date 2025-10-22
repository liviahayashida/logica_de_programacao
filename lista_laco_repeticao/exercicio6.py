print("Este programa identifica se o número é primo ou não")

numero = int(input("Digite um número inteiro: "))
for i in range(2, numero):
    if numero % i == 0:  
        print(f"O número {numero} não é primo")
        break
    else:
        print(f"O número {numero} é primo")

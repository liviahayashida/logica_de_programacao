print("Este programa verificar se é impar ou par e dependendo do resultado apresenta uma mudança")
numero = int(input("Digite um numero para a verificação: "))
for i in range (1, 21):
    if i%2==0:
        print(f"{i} é par")
        print(f"Este numero divido por 2 é {numero/2}")
    else:
        print(f"{i} é ímpar")
        print(f"Este numero multiplicado por 3 é {numero*3}")
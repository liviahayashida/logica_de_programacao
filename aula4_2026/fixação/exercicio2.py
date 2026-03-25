print("Este programa pede um número ao usuário e exibe os múltiplos desse número de 1 a 10")
num = int(input("Digite um número para exibimos seus múltiplos de 1 a 10: "))
for i in range (1,11):
    print(f"{num} x {i} = {num*i}")

print("Este programa exibe uma tabuada de 1 a 10, mas avisa quando o número for múltiplo de 3")
num = int(input("Digite um número: "))
for i in range (1,11):
    print(f"{num} x {i} = {num*i}")
    if (num*i)%3==0:
        print("⬆️   É multiplo de 3")

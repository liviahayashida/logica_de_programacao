print("Este programa exibe o fatorial de um número.")
num = int(input('Digite um número: '))
fatorial=1
for i in range (1, num +1):
    fatorial *=i
print(f"A fatorial é igual a {fatorial}")

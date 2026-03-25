print("Este programa exibe entre 1 e N quantos numeros sao multiplos de 3 e 5")
n = int(input("Digite o numero para final: "))
multiplos = 0
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        multiplos=multiplos+1
print(f"Temos {multiplos} multiplos de 3 e 5")
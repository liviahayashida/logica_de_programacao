print("Este programa encontra o maior numero inserido")
num = int(input("Digite seu primeiro numero: "))
maior = num
resposta = input("Digite sair para terminar e C caso queira continuar: ")
while resposta != "sair":
    num = int(input("Digite seu numero: "))
    resposta = input("Digite sair para terminar e C caso queira continuar: ")
    if num>maior:
        maior = num
print(f"O maior numero é {maior}")
    
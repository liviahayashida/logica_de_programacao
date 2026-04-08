print("Este programa converte a temperatura de Celsius para Fahrenheit")
resposta = ""

while resposta != "sair":
    celsius = float(input("Digite a temperatura: "))
    temp = (celsius*1.8)+32
    print(f"A temperatura em Fahrenheit é {temp}")

    resposta = input("Digite sair para terminar e C caso queira continuar: ")
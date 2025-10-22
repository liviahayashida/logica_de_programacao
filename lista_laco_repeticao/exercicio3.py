print("Este programa exibe uma tabuada deste número")
numero = int(input("Digite um número inteiro positivio: "))
tabuada = 0

for i in range (0, 10):
    tabuada= tabuada+1
    resultado = numero*tabuada
    print(f"{numero} x {tabuada} = {resultado}")
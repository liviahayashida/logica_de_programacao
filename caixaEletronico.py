print("Este programa simula um caixa eletronico")
saldo = float(input("Digite seu saldo: "))
while saldo>0:
    saque = float(input("Digite a quantidade que deseja sacar: "))
    saldo = saldo - saque
print(f"Seu atual saldo: {saldo}")
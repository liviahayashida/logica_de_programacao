print("Este programa simula um caixa eletronico")
saldo = float(input("Digite seu saldo atual: "))
opcao = input("Selecione uma opção, 1-sacar ou 2-depositar: ")
if opcao=='1':
    valor_saque = float(input("Digite o valor que deseja sacar: "))
    if valor_saque>saldo:
        print("Saldo insuficiente...")
    else:
        print(f"Voce sacou {valor_saque:.2f} reis, seu saldo atual é de {saldo-valor_saque:.2f}")
elif opcao=='2':
    valor_deposito = float(input("Digte a quantidade que deseja depositar:"))
    print(f"Voce depositou {valor_deposito:.2f} reais, seu novo saldo é de {saldo+valor_deposito:.2f}")
else:
    print("Opção inválida...Digite novamente")
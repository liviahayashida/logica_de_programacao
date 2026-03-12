
print("Este programa converte um valor em dólar, euro ou libra para reais")
escolha = int(input("Digite o número da opção escolhida: \n1. Dólar (USD); \n2. Euro (EUR); \n3. Libra(GBP): \n"))
quantidade = float(input("Digite a quantidade que deseja converter: \n"))


match escolha:
    case 1:
        print(f"{quantidade} dólares em reais é igual a {quantidade/5.19:.2f}")
    case 2:
        print(f"{quantidade} euros em reais é igual a {quantidade/6.03:.2f}")
    case 3:
        print(f"{quantidade} libras em reais é igual a {quantidade/6.98:.2f}")

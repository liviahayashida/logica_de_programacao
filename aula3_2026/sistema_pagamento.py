print("Este programa  simula um sistema de pagamento, informando se há desconto ou acréscimo em sua escolha")
escolha = int(input("Digite o número equivalente a escolha desejada: \n1. Crédito; \n2. Débito; n\n3. Dinheiro; \n"))

match escolha:
    case 1:
        print("No crédito voce terá um acréscimo de 5%")
    case 2:
        print("No débito voce terá 5% de desconto")
    case 3:
        print("No dinheiro voce não terá nem acréscimo nem desconto")
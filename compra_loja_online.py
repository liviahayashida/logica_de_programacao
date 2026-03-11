print("Este programa simula uma compra em uma loja online")
escolha_produto = int(input("Digite o número do produto escolhido para saber seu preço \n1. Salgadinho; \n2. Coca Cola; \n3. Café com leite; \n4. Pão de Queijo; \n"))

match escolha_produto:
    case 1:
        print("O salgadinho esta R$ 7,00")
    case 2:
        print("A Coca Cola esta R$ 8,00")
    case 3:
        print("O café com leite esta R$ 9,00")
    case 4:
        print("O pão de queijo esta R$ 5,00")
        
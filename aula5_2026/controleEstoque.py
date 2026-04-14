print("Este programa controla um estoque")

opcao = ""
listaProdutos = []
while opcao != "3":
    print("1 - Adicionar produto\n2 - Exibir\n3 - Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        produto = input("Digite seu produto: ")
        listaProdutos.append(produto)
    elif opcao == "2":
            print(f"Produtos adicionados: {listaProdutos}")
print("Programa encerrado")
print("Este programa simula uma caixa registradora")

opcao = ""
valor_total  = 0
listaProdutos = []
while opcao != 2:
    print("1 - Adicionar produto\n2 - Sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao != 2:
        produto = input("Digite seu produto: ")
        listaProdutos.append(produto)
        quantidade = int(input("Digite a quantidade desejada deste produto: "))
        preco = float(input("Digite o preço do produto: "))
        valor_total= valor_total+(quantidade*preco)
print(f"Sua compra foi finalizada.\nProdutos adicionados: {listaProdutos}\nSua compra esta no valor de: {valor_total}")
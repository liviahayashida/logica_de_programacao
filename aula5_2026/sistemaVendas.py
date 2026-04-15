print("Este programa simula um sistema de vendas e estoque")

opcao = ""
quantidade = 0
quant_atual = 0
while opcao != "3":
    print("1 - Adicionar quantidade \n2 - Vender\n3 - Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        quantidade = int(input("Digite a quantidade do produto: "))
        quant_atual=quantidade+quant_atual
    elif opcao == "2":
        if quantidade<=0:
            opcao="3"
            print("Seu estoque chegou ao fim!")
        else:
            retirar = int(input("Digite a quantidade de produto que voce vendeu: "))
            quantidade=quantidade-retirar
            
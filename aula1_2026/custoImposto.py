print("Este programa calcula o custo de um carro novo e seus impostos")
preco_carro = float(input("Digite o preço do carro: "))
print(f"O valor a ser pago pelo carro, com os impostos e porcentagem do distribuidor é de {preco_carro + (preco_carro * 0.28) + (preco_carro * 0.45):.2f} reais")
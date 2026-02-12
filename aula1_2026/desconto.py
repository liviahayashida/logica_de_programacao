print("Este programa aplica um desconto de 10% em um produto")
preco_produto = float(input("Digite o preço do produto: "))
print(f"Seu desconto será de {preco_produto*0.1:.2f}, e seu preco final vai ser de {preco_produto - (preco_produto*0.1):.2f}")
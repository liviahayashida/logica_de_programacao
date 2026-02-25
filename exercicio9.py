print("Este programa aplica um desconto se o produto custar mais que 100 reais")
preco = float(input("Digite o preco do produto: "))
if preco>100:
    print(f"Voce terá um desconto de {preco-(preco*0.10)}")
else:
    print("Infelizmente voce não terá desconto...")
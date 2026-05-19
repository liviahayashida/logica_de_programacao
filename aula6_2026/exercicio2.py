print("Este programa armazena 5 nomes em uma lista e exibe um por um")
nomes = []
for i in range(5):
    nome = input("Digite um nome: ")
    nomes.append(nome)
print(f"Os nomes digitados foram: {nomes}")

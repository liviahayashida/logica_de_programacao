print("Este programa busca nomes atraves de um vetor")
nomes = []

for i in range(0, 5):
    nome = input(f"Digite o {i+1}° nome: ").lower() 
    nomes.append(nome)

buscar = input("Digite um nome para buscar: ").lower()

if buscar in nomes:
    print(f"O nome {buscar} está na lista")
else:
    print("O nome não está na lista")
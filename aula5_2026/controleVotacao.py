print("Este programa controla uma votação. Digite fim para sair \n1 - candidato 1\n2 - candidato 2\n3 - candidato 3")

opcao = ""
cand1 = 0
cand2 = 0
cand3 = 0
while opcao != "fim":
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cand1 += 1
    elif opcao == "2":
        cand2 += 1
    elif opcao == "3":
        cand3 += 1
print(f"Programa encerrado\nCandidato 1: {cand1}\nCandidato 2: {cand2}\nCandidato 3: {cand3}")
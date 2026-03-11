print('Este programa simula um sistema de reserva de passagens de onibus')
escolha = int(input("Digite o número da opção desejada para saber o valor da passagem: \n1. São Paulo; \n2. Rio de Janeiro; \n3. Curitiba; \n4. Salvador; \n "))

match escolha:
    case 1:
        print(" A passagem de indaiatuba para São Paulo de onibus é de 52,35 R$")
    case 2:
        print('A passagem de indaiatuba para o Rio de Janeiro 200,00 R$')
    case 3:
        print("A passagem de indaiatuba para Curitiba é de 210 R$")
    case 4:
        print("A passagem de indaiatuba para Salvador é de 550 R$")
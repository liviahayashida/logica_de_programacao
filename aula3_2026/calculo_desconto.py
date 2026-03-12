print("Este programa exibe um porcentual de desconto de acordo com o tipo de produto desejado")
escolha_produto = int(input("Digite o número da opção escolhida: \n1. Eletronico; \n2. Roupas; \n3. Alimentos; \n4. Móveis; \n"))

match escolha_produto:
    case 1:
        print("O seu desconto será de 10%")
    case 2:
        print("O seu desconto será de 10%, no mínimo 2 peças")
    case 3:
         print('Seu desconto de 5%')
    case 4:
        print("Seu desconto será de 15%")

print("Este sistema simula um atendimento telefonico")
escolha = int(input("Digite o número equivalente a opção desejada:\n1. Suporte Técnico; \n2. Financeiro; \n3. Cancelamento; \n4. Falar com um atendente; \n"))

match escolha:
    case 1:
        print("Espere para seu auxilio no suporte técnico")
    case 2:
        print('Aguarde para seu atendimento financeiro')
    case 3:
        print('Seu cancelamento será efetuado em breve, espere para mais informações')
    case 4:
        print('Encaminharemos voce para uma atendente. Aguarde...')
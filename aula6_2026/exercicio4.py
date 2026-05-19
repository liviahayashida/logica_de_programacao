print("Este programa soma todos os elementos de uma lista de inteiros digitados pelo usuário")
print("Digite 'p' para parar de digitar\n")

numeros = []
soma = 0

num = input("Digite um número: ")

while num.lower() != "p":
    numero_inteiro = int(num)
    
    numeros.append(numero_inteiro)
    soma = soma + numero_inteiro
    
    print(f"A soma dos números atual é: {soma}")
    print(f"Seus números digitados foram: {numeros}\n")

    num = input("Digite um número: ")

print("\nPrograma encerrado!")
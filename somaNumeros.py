print("Este programa solicita ao usuário numeros e soma esses numeros até que o usuario insira zero, ao final mostra a soma total")
soma = 0
num = int(input("Digite um número: (digite 0 para sair) "))
soma = soma+num
while num != 0:
    num = int(input("Digite um numero: "))
    soma = soma+num
print(f"A soma dos numeros é igual a: {soma}")
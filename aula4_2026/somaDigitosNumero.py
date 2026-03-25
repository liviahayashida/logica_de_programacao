print("Este programa pede um número e soma seus dígitos.")
numero = input("Digite um número: ")
soma = 0
for digito in numero:
    soma += int(digito)
print("Soma dos digitos:", soma)

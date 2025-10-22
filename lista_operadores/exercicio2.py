print("Este programa mostra a divisão inteira e a divisão real")
number1 = float(input("Digite um número inteiro: "))
number2 = float(input("Digite seu segundo número inteiro: "))

divisaoreal = number1/number2
divisaointeira = number1//number2
diferenca = divisaoreal - divisaointeira

print(f"Divisão real: {divisaoreal}")
print(f"Divisao inteira: {divisaointeira}")
print(f"Diferença entre os resultados: {diferenca}")
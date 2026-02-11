print("Este programa mostra se dois números são múltiplos ou não")
num1 = int(input("Digite seu primerio número: "))
num2 = int(input("Digite seu segundo número: "))
if num1%num2==0 or num2%num1==0:
    print("Os números são múltiplos")
else:
    print("Os números não são múltiplos")
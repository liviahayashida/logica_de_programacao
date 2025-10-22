print("Este programa verifica o tipo de triangulo")
lado1 = float(input("Digite o valor do lado 1: "))
lado2 = float(input("Digite o valor do lado 2: "))
lado3 = float(input("Digite o valor do lado 3: "))

if (lado1==lado2 and lado2==lado3):
     print ("O triangulo é um equilátero!")
elif(lado1!=lado2 and lado2!=lado3 and lado1!=lado3):
     print("O triangulo é um escaleno!")
else:
     print("O triangulo é um isósceles!")
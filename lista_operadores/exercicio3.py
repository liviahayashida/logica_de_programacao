print("Este programa calcula o resto da divisão por diversos números")
number = float(input("Digite um número: "))

restodivisaopor2 = number%2
restodivisaopor3 = number%3
restodivisaopor5 = number%5
restodivisaopor10 = number%10

if restodivisaopor2 == 0:
     print ("Número PAR!")
else: print("Número ÍMPAR!")
print(f"Resto da divisão por 2: {restodivisaopor2}")
print(f"Resto da divisão por 3: {restodivisaopor3}")
print(f"Resto da divisão por 5: {restodivisaopor5}")
print(f"Resto da divisão por 10: {restodivisaopor10}")

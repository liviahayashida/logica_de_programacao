print("Este programa mostra 10 numeros, e quantos sao positivos, negativos e zero")
positivos = 0
negativos = 0
zero = 0
for i in range (10):
    numero = int(input(f"Digite seu {i+1} numero: "))
    if numero == 0:
        zero=zero+1
    elif numero<0:
        negativos=negativos+1
    elif numero>0:
        positivos=positivos+1
print(f"Temos {positivos} numeros positivos")
print(f"Temos {negativos} numeros negativos")
print(f"Temos {zero} zeros")
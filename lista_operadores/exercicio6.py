print("Este programa calcula resultados com valores booleanos com OR")
A = input("Digite um valor booleano (True ou False): ").lower() == "true"
B = input("Digite seu segundo valor booleano (True ou False): ").lower() == "true"
C = input("Digite seu terceiro valor booleano (True ou False): ").lower() == "true"
D = input("Digite seu quarto valor booleano (True ou False): ").lower() == "true"

print(A or B)
print(C or D)
print(A or B or C)
print(A or B or C or D)
print((A or B) or (C or D))
print("Este programa calcula resultados com valores booleanos com OR")
A = input("Digite um valor booleano (True ou False): ").lower() == "true"
B = input("Digite seu segundo valor booleano (True ou False): ").lower() == "true"
C = input("Digite seu terceiro valor booleano (True ou False): ").lower() == "true"

print(not A)
print(not B)
print(not C)
print(not (A and B))
print(not (A or B))
print(not A and not B)
print(not (not A))
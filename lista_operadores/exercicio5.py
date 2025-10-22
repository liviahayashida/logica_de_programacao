print("Este programa calcula resultados com valores booleanos com AND")
A = input("Digite um valor booleano (True ou False): ").lower() == "true"
B = input("Digite seu segundo valor booleano (True ou False): ").lower() == "true"
C = input("Digite seu terceiro valor booleano (True ou False): ").lower() == "true"
D = input("Digite seu quarto valor booleano (True ou False): ").lower() == "true"

# A = bool(input("Digite um valor booleano"))
# B = bool(input("Digite seu segundo valor booleano"))
# C = bool(input("Digite seu terceiro valor booleano"))
# D = bool(input("Digite seu quarto valor booleano"))

print(A and B)
print(C and D)
print(A and B and C)
print(A and B and C and D)
print((A and B) and (C and D))


print("Este programa calcula a area a ser pintada e a quantidade de tinta necessaria para o serviço")
altura = float(input("Digite a altura da parede em metros:"))
largura = float(input("Digite a largura da parede em metros: "))
print(f"A area a ser pintada é de {altura*largura:.2f} metros quadrados, e a quantidade de tinta necessaria para o serviço é de {(altura*largura)/2:2f} litros")
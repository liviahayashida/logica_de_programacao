print("Este programa calcula o valor dos serviços de uma locadora")
km_percorridos = float(input("Digite a quantidade de km percorridos:"))
dias = int(input("Digite a quantidade de dias que o carro ficou alugado:"))
print(f"O valor a ser pago será de: {(90*dias)+ (0.20*km_percorridos):.2f} reais")
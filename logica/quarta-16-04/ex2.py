# 2. Simular o abastecimento de um tanque de combustível. 
# Peça ao usuário quantos litros ele gostaria de abastecer e simule o abastecimento litro a litro.
# Escolha a estrutura de repetição adequada e faça a representação em fluxograma e python.

print ("Simulação de abastecimento de tanque de combustível")
litros = int(input("Quantos litros deseja abastecer? "))
tanque = 0
for i in range(litros):
    tanque += 1
print(f"Tanque abastecido com {litros} litros.")
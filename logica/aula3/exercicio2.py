# 2. Verificação de Idade
#Peça ao usuário sua idade e use uma estrutura condicional para informar se ele pode votar e se o voto é obrigatório,
# se ele não pode votar ou se o voto é opcional.

idade = int(input("Digite sua idade: "))
if idade < 16:
    print("Você não pode votar")
elif idade < 18 or idade >= 70:
    print("Seu voto é opcional")
else:
    print("Seu voto é obrigatório")


# o também uma forma mais limap e correta:

idade = int(input("Digite sua idade: "))
if idade < 16:
    print("Você não pode votar")
elif 18<= idade < 70:
    print("Seu voto é obrigatório")
else:
    print("Seu voto é opcional")
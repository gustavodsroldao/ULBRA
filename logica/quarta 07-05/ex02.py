# Busca e Condicional
# Peça ao usuário para digitar uma fruta.
# Verifique se ela está na lista (use if).
# Se estiver, imprima "A fruta está na lista".

item = input("Digite o nome de uma fruta: ")
lista = ["maçã", "banana", "laranja", "uva", "abacaxi"]
if item in lista:
    print("A fruta está na lista")
else:
    print("A fruta não está na lista")
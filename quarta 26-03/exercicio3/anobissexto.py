# 3. Verificar se um ano é bissexto
# Peça ao usuário um ano e verifique se ele é bissexto (um ano bissexto deve ser divisível por 4 ou por 100 e 400). Mostre a resposta em tela.
# Faça o fluxograma do algoritmo e depois o escreva em Python.

ano = int(input("Digite um ano: "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("Ano bissexto")
else:
    print("Ano não bissexto")
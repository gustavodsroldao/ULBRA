# Só pode usar:
# - Funções (def)
# - Condicionais (if, else)
# - Repetições (for, while)
# - Listas (vetores e matrizes)
# Escreva uma função que gere uma matriz identidade de ordem 5
# Em matemática, matriz identidade é uma matriz diagonal, cujos elementos da diagonal principal são todos iguais. Sua função, então, deve criar uma matriz 7x7 preenchida com 0, mas sua diagonal deve ser preenchida com 1.
def matriz_identidade():
    matriz = []
    for i in range(7):
        linha = []
        for j in range(7):
            if i == j:
                linha.append(1)
            else:
                linha.append(0)
        matriz.append(linha)
    return matriz

identidade = matriz_identidade()
for linha in identidade:
    print(linha)

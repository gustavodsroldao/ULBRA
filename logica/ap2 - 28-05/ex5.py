# Só pode usar:
# - Funções (def)
# - Condicionais (if, else)
# - Repetições (for, while)
# - Listas (vetores e matrizes)
# Crie uma função que receba uma matriz 7x4 e retorne um vetor com a média de cada linha. 
def medias_por_linha(matriz):
    medias = []
    for linha in matriz:
        soma = 0
        count = 0
        for valor in linha:
            soma += valor
            count += 1
        media = soma / count 
        medias.append(media)
    return medias
    
matriz_exemplo = [
    [4, 6, 8, 2],
    [3, 5, 7, 1],
    [9, 2, 4, 6],
    [5, 3, 8, 7],
    [1, 2, 3, 4],
    [6, 5, 4, 3],
    [2, 8, 6, 4]
]

medias = medias_por_linha(matriz_exemplo)
for i, media in enumerate(medias):
    print(f"Média da linha {i + 1}: {media:.2f}")
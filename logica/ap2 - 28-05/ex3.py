# Só pode usar:
# - Funções (def)
# - Condicionais (if, else)
# - Repetições (for, while)
# - Listas (vetores e matrizes)

def maior_valor_e_indice(lista):
    if not lista:
        return None, None
    maior_valor = lista[0]
    indice = 0
    for numero in lista:
        if numero > maior:
            maior = numero
            indice_maior = i
        i += 1
    return maior_valor, indice

numeros = [3, 5, 2, 8, 1]
maior, indice = maior_valor_e_indice(numeros)
print("O maior valor é:", maior)
print("O índice do maior valor é:", indice)
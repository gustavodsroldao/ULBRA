# Só pode usar:
# - Funções (def)
# - Condicionais (if, else)
# - Repetições (for, while)
# # - Listas (vetores e matrizes)
# Crie uma função que verifica se um número está presente em um vetor e retorna a sua posição.

def encontrar_numero(vetor, numero):
    i = 0
    while True:
        try:
            if vetor[i] == numero:
                return i
            i = i +1
        except IndexError:
            break
    return -1

vetor = [3, 7, 1, 9, 5]
numero = 9

posicao = encontrar_numero(vetor, numero)

if posicao != -1:
    print(f"O número {numero} está na posição {posicao} do vetor.")
else:
    print(f"O número {numero} não está presente no vetor.")
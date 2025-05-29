# Só pode usar:
# - Funções (def)
# - Condicionais (if, else)
# - Repetições (for, while)
# - Listas (vetores e matrizes)
# Crie uma função que receba um vetor de inteiros e um número x, e retorne quantas vezes x aparece no vetor.  
def vetor_inteiros(vetor, x):
    contador = 0
    for numero in vetor:
        if numero == x:
            contador += 1
    return contador

vetor = [1, 2, 3, 2, 4, 2]
x = 2
print(vetor)
print("A quantidade de vezes que o número X aparece no vetor é: ", vetor_inteiros(vetor, x))

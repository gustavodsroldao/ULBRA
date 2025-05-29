# Só pode usar:
# - Funções (def)
# - Condicionais (if, else)
# - Repetições (for, while)
# - Listas (vetores e matrizes)
# Crie uma função que receba um vetor de números inteiros e retorne a soma apenas dos números ímpares.  

def soma_impares(vetor):
    soma = 0
    for numero in vetor:
        if numero % 2 != 0:  # Verifica se o número é ímpar
            soma += numero
    return soma

# Exemplo de uso
vetor_exemplo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
resultado = soma_impares(vetor_exemplo)
print("A soma dos números ímpares é:", resultado)

# Versão 2 (Com input do usuário)
def soma_impares(entrada):
    numero = ''
    lista = []
    for caractere in entrada:
        if caractere != '':
            numero += caractere
        elif numero:
            lista.append(int(numero))
            numero = ''
    if numero:
        lista.append(int(numero))
    return sum(i for i in lista if i %2 != 0)

# Solicita ao usuário uma lista de números inteiros
entrada = input("Digite uma lista de números inteiros: ")
resultado = soma_impares(entrada)
print("A soma dos números ímpares é:", resultado)
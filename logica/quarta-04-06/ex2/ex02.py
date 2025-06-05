# Crie uma função soma_pares(lista) que receba uma lista de números
# e retorne a soma de todos os valores pares. Use outra função auxiliar
# eh_par(numero)
# para verificar se o número é par.

def soma_pares(lista):
    lista = [elemento for elemento in lista if eh_par(elemento)] # Percorre cada 'elemento' da lista e verifica se eh_par(elemento)
    return sum(lista)

def eh_par(numero):
    return numero % 2 == 0

print (soma_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) # Exemplo de uso da função soma_pares
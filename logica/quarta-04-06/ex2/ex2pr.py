def soma_pares(lista):
    lista = [e for e in lista if eh_par(e)]
    return sum(lista)

def eh_par(numero):
    return numero % 2 == 0

print(soma_pares([0, 1 , 2 ,3 ,4 ,5 ,6 ,7, 8, 9, 10]))
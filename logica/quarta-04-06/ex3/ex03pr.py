def calcular_media(lista_de_notas):
    soma = sum(lista_de_notas)
    qnt_notas = len(lista_de_notas)
    media = soma / qnt_notas
    return media

def avaliar_desempenho(media):
    if media >= 6:
        print("Aprovado")
    elif 0 < media < 6:
        print("Recuperação")
    else:
        print('Reprovou')

lista = [6, 2, 8]
media = calcular_media(lista)
avaliar_desempenho(media)
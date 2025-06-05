def calcular_media(lista_de_notas):
    quantidade_notas = len(lista_de_notas)
    soma_notas = sum(lista_de_notas)
    media = soma_notas / quantidade_notas
    return media
   
def avaliar_desempenho(media):
    if media >= 6:
        print('Aprovado')
    elif 0 < media < 6:
        print('Recuperação semestral')
    else:
        print('reprovou')

notas = [2, 1 , 7]
media = calcular_media(notas)
avaliar_desempenho(media)
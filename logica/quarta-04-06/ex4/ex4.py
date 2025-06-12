# Crie uma função remover_duplicados(lista) que retorne uma nova lista com os elementos únicos da lista original, mantendo a ordem de aparição.

def remover_duplicados(lista):
    return list(set(lista))

# Testando a função
lista_original = [1, 2, 2, 3, 4, 4, 4, 5]
lista_sem_numeros_duplicados = remover_duplicados(lista_original)
print(lista_sem_numeros_duplicados)  # Saída esperada: [1, 2, 3, 4, 5]
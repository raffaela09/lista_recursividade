'''Escreva uma função recursiva chamada indice_maior_elemento(lista) que retorna o
índice do maior elemento em uma lista.
Exemplo de Entrada:
indice_maior_elemento([1, 5, 3, 9, 2])
Saída Esperada:
3 # O maior elemento é 9, que está no índice 3'''

lista_one = [1, 5, 3, 9, 2]

def sum_list(lista):
    if len(lista) == 1:
        return lista[0]
    item = sum_list(lista[1:])
    # item_enumerate = sum_list(enumerate(lista))
    return lista[0] if lista[0] > item else item

result = sum_list(lista_one)
print(result)
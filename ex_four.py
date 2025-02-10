'''Escreva uma função recursiva chamada indice_maior_elemento(lista) que retorna o
índice do maior elemento em uma lista.
Exemplo de Entrada:
indice_maior_elemento([1, 5, 3, 9, 2])
Saída Esperada:
3 # O maior elemento é 9, que está no índice 3'''

lista_one = [1, 5, 3, 9, 2]

def indice_maior_elemento(lista, indice=0, maior_indice=0):
    if indice == len(lista):
        return maior_indice
    if lista[indice] > lista[maior_indice]:
        maior_indice = indice
    return indice_maior_elemento(lista, indice + 1, maior_indice)

resultado = indice_maior_elemento(lista_one)
print(resultado)
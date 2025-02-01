'''Exercício 1: Reverter os Caracteres de uma String
Escreva uma função recursiva chamada reverter_caracteres(s) que recebe uma
string s e devolve a string invertida. Não use laços (for ou while).
Exercício 2: Soma de Números em uma Lista Aninhada
Implemente uma função recursiva chamada soma_lista_aninhada(lista) que calcula a
soma de todos os números em uma lista, mesmo que os números estejam dentro de
sublistas (listas aninhadas).
Exemplo de Entrada:
soma_lista_aninhada([1, [2, 3], [4, [5]]])
Saída Esperada:
15 # (1 + 2 + 3 + 4 + 5)'''

list_one = [1, [2, 3], [4, [5]]]

def sum_list(lista):
    if len(lista) == 0:
        return 0
    item_one = lista[0]
    list_full = lista[1:]
    if isinstance(item_one, list): #verifica se o item é uma lista para que prossiga.
        return sum_list(item_one) + sum_list(list_full)
    else: 
        return item_one + sum_list(list_full)
    
result = sum_list(list_one)
print(f'A soma dos itens da lista {list_one} é: {result}')
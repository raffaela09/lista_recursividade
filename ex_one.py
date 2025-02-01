'''Exercício 1: Reverter os Caracteres de uma String
Escreva uma função recursiva chamada reverter_caracteres(s) que recebe uma
string s e devolve a string invertida. Não use laços (for ou while).'''

def invert(word):
    if len(word) <= 1:
        return word
    
    return  word[-1] + invert(word[:-1])

execut = invert('rafa')

print(execut)
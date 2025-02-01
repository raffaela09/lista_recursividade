'''Crie uma função recursiva chamada contar_caracteres(s, c) que conta quantas vezes o
caractere c aparece na string s.
Exemplo de Entrada:
contar_caracteres("banana", "a")
Saída Esperada:
3'''

def count_letter(word, letter):
    if len(word) == 0:
        return 0
    if word[0] == letter:
        return 1 + count_letter(word[1:], letter)
    
    return count_letter(word[1:], letter)

camp = input('Digite a palavra: ').lower()
camp2 = input('Digite a letra que vc deseja contar: ').lower()
result = count_letter(camp, camp2)
print(result)
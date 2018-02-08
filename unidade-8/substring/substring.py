# coding: utf-8
# Laboratório de Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Substring - Unidade 8


# Retorna o índice da letra na string, caso exista na string.
def existe_letra(letra, string, inicio):
    for i in range(inicio, len(string)):
        if string[i] == letra:
            return i

    return -1


# Verifica se a string2 é substring da string1.
def is_substring(string1, string2):
    substring = ''
    i = 0

    for letra in string2:
        indice = existe_letra(letra, string1, i)

        if indice != -1:
            i = indice + 1
            substring += letra

            if substring == string2:
                return True
        else:
            return False
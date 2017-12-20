# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Flip - Unidade 7


# Reverte os elementos de uma lista que
# estão entre as posições i e j, inclusive.
def flip(lista, i, j):
    while i <= j:
        lista[i], lista[j] = lista[j], lista[i]
        i += 1
        j -= 1

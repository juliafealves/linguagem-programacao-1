# coding: utf-8
# Laboratório de Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Insere Primeiro - Unidade 7


# Retorna uma lista ordenada, onde ordena
# somente o primeiro elemento.
def insere_ordenado_primeiro(lista):
    primeiro = lista[0]

    for i in range(1, len(lista)):
        if primeiro > lista[i]:
            lista[i-1], lista[i] = lista[i], lista[i-1]

    return lista

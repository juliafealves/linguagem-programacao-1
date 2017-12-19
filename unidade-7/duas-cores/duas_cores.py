# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Duas Cores - Unidade 7


# Altera o lista inicial, trazendo todos os elementos
# da cor1 para o início da lista e deixando todos os
# elementos da cor2 no final da lista.
def separa_duas_cores(lista, cor1, cor2):
    tamanho = len(lista)
    i = 0
    posicao = 0

    while i < tamanho:
        for j in range(i, tamanho):
            if lista[j] == cor1:
                auxiliar = lista[posicao]
                lista[posicao] = lista[j]
                lista[j] = auxiliar
                i = j + 1
                posicao += 1
            else:
                i += 1


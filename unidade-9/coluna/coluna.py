# coding: utf-8
# Laboratório de Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Coluna - Unidade 9


# Retorna uma nova lista de acordo com os elementos do
# array localizado na coluna informado.
def coluna(matriz, coluna):
    lista = []

    for i in range(len(matriz)):
        lista.append(matriz[i][coluna])

    return lista

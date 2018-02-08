# coding: utf-8
# Laboratório de Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Busca Todos - Unidade 9


# Retorna as posições que um elemento se encontra numa lista.
def obter_posicoes_elemento(lista, elemento):
    posicoes = []

    for indice in range(len(lista)):
        if lista[indice] == elemento:
            posicoes.append(indice)

    return posicoes


# Retorna as posições que o elemento se encontra na matriz.
def busca_matriz(matriz, elemento):
    posicoes = []

    for i in range(len(matriz)):
        indices = obter_posicoes_elemento(matriz[i], elemento)

        if len(indices) > 0:
            for indice in indices:
                localizacao = (i, indice)
                posicoes.append(localizacao)

    return posicoes

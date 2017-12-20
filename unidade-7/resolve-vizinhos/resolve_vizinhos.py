# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Resolve Vizinhos - Unidade 7


# Altera a lista quando encontra valores consecutivos
# iguais e alterando o valor mais à esquerda, incrementando-o
# até que seja diferente dos seus dois vizinhos.
def resolve_vizinhos(lista):
    atual = lista[0]
    anterior = None

    for indice in range(1, len(lista)):
        proximo = lista[indice]

        while atual == proximo or atual == anterior:
            atual += 1
            lista[indice - 1] = atual

        atual = lista[indice]
        anterior = lista[indice - 1]

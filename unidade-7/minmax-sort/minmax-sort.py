# coding: utf-8
# Laboratório de Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: MinMax Sort - Unidade 7


# Retorna o índice onde existe o menor número.
# O parâmetro inicial, final delimita a faixa de comparação da lista.
def menor_elemento(lista, inicial, final):
    menor = lista[inicial]
    indice = inicial

    for i in range(inicial + 1, final + 1):
        if menor > lista[i]:
            menor = lista[i]
            indice = i

    return indice


# Retorna o índice onde existe o maior número.
# O parâmetro inicial, final delimita a faixa de comparação da lista.
def maior_elemento(lista, inicial, final):
    maior = lista[inicial]
    indice = inicial

    for i in range(inicial + 1, final + 1):
        if maior < lista[i]:
            maior = lista[i]
            indice = i

    return indice


# Retorna a cópia de uma lista.
def copia_lista(lista):
    copia = []

    for elemento in lista:
        copia.append(elemento)

    return copia


# Realiza a troca de dois índices numa lista.
def troca_elementos(lista, indice_1, indice_2):
    lista[indice_1], lista[indice_2] = lista[indice_2], lista[indice_1]


# Retorna uma lista de elementos organizados através do algoritmo MinMax Sort.
def minmax_sort(lista):
    listas = []
    i = 0
    j = len(lista) - 1

    while i < j:
        menor = menor_elemento(lista, i, j)
        troca_elementos(lista, i, menor)
        i += 1

        maior = maior_elemento(lista, i, j)
        troca_elementos(lista, j, maior)
        j -= 1

        listas.append(copia_lista(lista))

    return listas
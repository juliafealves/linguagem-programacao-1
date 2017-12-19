# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Filtra e Altera Lista - Unidade 7


# Altera a lista removendo os elementos cujos índices
# não são divisíveis por "numero".
def filtra_altera_lista(numero, lista):
    lista_auxiliar = []

    for elemento in lista:
        lista_auxiliar.append(elemento)

    removidos = 0
    for indice in range(len(lista_auxiliar)):
        if indice % numero != 0:
            lista.pop(indice - removidos)
            removidos += 1
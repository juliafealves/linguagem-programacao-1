# coding: utf-8
# Laboratório de Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Soma Moldura - Unidade 9


# Retorna a soma das extremidades de uma lista.
def somar_extremidades(lista, inicio, fim):
    return lista[inicio] + lista[fim]


# Retorna a soma dos números de uma lista.
def somar_elementos(numeros, inicio, fim):
    soma = 0

    for i in range(inicio, fim):
        soma += numeros[i]

    return soma


# Retorna soma dos elementos da moldura de uma matriz quadrada de acordo com o nível.
def soma_moldura(matriz, nivel):
    ultima_linha = len(matriz) - nivel
    soma = 0

    for i in range(nivel, ultima_linha):
        inicio = nivel
        final = len(matriz[i]) - nivel

        if i == nivel or i == (ultima_linha - 1):
            soma += somar_elementos(matriz[i], inicio, final)
        else:
            soma += somar_extremidades(matriz[i], inicio, final - 1)

    return soma

# coding: utf-8
# Laboratório de Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Soma Intervalo - Unidade 6


# Retorna a soma dos inteiros entre um número a e
# um número b, inclusive estes números.
def soma_intervalo(a, b):
    resultado = a

    for numero in range(a + 1, b + 1):
        resultado += numero

    return resultado

# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Conta Palavras - Unidade 7


# Retorna a quantidade de palavras com
# comprimento maior ou igual a "tamanho".
# Recebe como parâmetro um inteiro "tamanho e
# uma string("palavras") com palavras separadas por ":".
def conta_palavras(tamanho, palavras):
    palavras = palavras.split(':')
    conta_palavra = 0

    for palavra in palavras:
        if len(palavra) >= tamanho:
            conta_palavra += 1

    return conta_palavra
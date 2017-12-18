# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Maior Palavra de Uma Frase - Unidade 6


# Retorna a maior palavra de um frase.
# Caso tenha mais de uma palavra maior, a última será retornada.
def maior_palavra(frase):
    # Artifício para contabilizar a última palavra.
    frase += ' '

    maior_palavra = ''
    palavra = ''

    for letra in frase:
        if letra != ' ':
            palavra += letra
        else:
            if len(maior_palavra) <= len(palavra):
                maior_palavra = palavra

            palavra = ''

    return maior_palavra
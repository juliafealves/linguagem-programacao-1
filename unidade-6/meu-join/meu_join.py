# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Meu Join - Unidade 6

# Concatena os caracteres da sequência com o delimitador informado.
# Não inclui o delimitador no último caracter.
def meu_join(delimitador, sequencia_string):
    nova_string = ""

    for indice in range(len(sequencia_string)):
        if indice == (len(sequencia_string) - 1):
            nova_string += sequencia_string[indice]
        else:
            nova_string += sequencia_string[indice] + delimitador

    return nova_string

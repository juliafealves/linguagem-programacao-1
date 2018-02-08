# coding: utf-8
# Laboratório de Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Altera Vetor - Unidade 8


# Altera as coordenadas de um vetor multiplicando por um escalar.
def altera_vetor_por_escalar(vetor, escalar):
    for i in range(len(vetor)):
        vetor[i] *= escalar


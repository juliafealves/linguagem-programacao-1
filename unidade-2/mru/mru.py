# coding: utf-8
# MRU 2
# (C) 2017, Júlia Alves / UFCG Programação 1

# Entrada dos dados.
posicao_inicial = float(raw_input())
velocidade = float(raw_input())
tempo = float(raw_input())

# Calculando a posição final.
posicao_final = posicao_inicial + (velocidade * tempo)

# Imprimindo os resultados
print "%.2f" % posicao_final
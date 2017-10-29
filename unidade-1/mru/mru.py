# coding: utf-8
# MRU
# (C) 2017, Júlia Alves / UFCG Programação 1

# Entrada dos dados.
posicao_inicial = float(raw_input())
velocidade = float(raw_input())
tempo = float(raw_input())

# Calculando a posição final.
posicao_final = posicao_inicial + (velocidade * tempo)

# Imprimindo os resultados
print "Posição final do móvel"
print "S(%.1f) = %.1f m" % (tempo, posicao_final)
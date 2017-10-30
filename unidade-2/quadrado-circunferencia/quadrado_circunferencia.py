# coding: utf-8
# Quadrado na Circunferência
# (C) 2017, Júlia Alves / UFCG Programação 1

import math

# Entrada dos dados.
raio = float(raw_input())

# Calculando a área da circunferência
area_circulo = math.pi * (raio ** 2)

# Encontrado o lado do quadrado atraves da diagonal.
lado = (raio * 2) / math.sqrt(2)

# Calculando a área do quadrado
area_quadrado = lado ** 2

# Calculando a área restante
area_restante =area_circulo - area_quadrado

# Imprimindo.
print "Área não comum: %.5f" % area_restante
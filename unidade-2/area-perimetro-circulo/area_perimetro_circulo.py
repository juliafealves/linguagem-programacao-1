# coding: utf-8
# Área e Perímetro de um Círculo
# (C) 2017, Júlia Alves / UFCG Programação 1

import math

# Entrada dos dados
diametro = int(raw_input())

# Calculando a área e o perímetro.
raio = diametro / 2.0
area = math.pi * (raio ** 2)
perimetro = 2 * math.pi * raio

# Imprimindo a área e o perímetro.
print "A: %.5f" % area
print "P: %.5f" % perimetro

# coding: utf-8
# Área do Círculo
# (C) 2017, Júlia Alves / UFCG Programação 1

import math

# Entrada de dado referente ao raio do circulo
raio = float(raw_input())

# Calculando a área
area = math.pi * (raio ** 2)

# Imprimindo o resultado da área.
print "%.2f" % area
# coding: utf-8
# Perímetro de um Triângulo
# (C) 2017, Júlia Alves / UFCG Programação 1

import math

# Entrada dos dados.
x1 = float(raw_input())
y1 = float(raw_input())
x2 = float(raw_input())
y2 = float(raw_input())
x3 = float(raw_input())
y3 = float(raw_input())

# Calculando as distâncias dos pontos
distancia1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
distancia2 = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
distancia3 = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)

# Calculando o perímetro do triângulo.
perimetro = distancia1 + distancia2 + distancia3

# Imprimindo.
print "O perímetro é de %.2f" % perimetro

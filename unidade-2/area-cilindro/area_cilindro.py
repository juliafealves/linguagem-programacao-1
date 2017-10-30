# coding: utf-8
# Área do Cilindro
# (C) 2017, Júlia Alves / UFCG Programação 1

import math

# Entrada dos dados
print "Cálculo da Superfície de um Cilindro\n---"
diametro = float(raw_input("Medida do diâmetro? "))
altura = float(raw_input("Medida da altura? "))

# Calculando a área do cilindro.
raio = diametro / 2.0
area_circulo = math.pi * (raio ** 2)
perimetro = 2 * math.pi * raio
area_retangulo = perimetro * altura

area_cilindro = 2 * area_circulo + area_retangulo

# Imprimindo a área do cilindro.
print "---\nÁrea calculada: %.2f" % area_cilindro

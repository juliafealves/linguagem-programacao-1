# coding: utf-8
# Caixas de Cerâmica
# (C) 2017, Júlia Alves / UFCG Programação 1

import math

# Entrada dos dados.
capacidade = float(raw_input("Capacidade de revestimento? "))
print "\n== Dados do vão a revestir =="
comprimento = float(raw_input("Comprimento? "))
largura = float(raw_input("Largura? "))
altura = float(raw_input("Altura? "))

# Calculando a área total
area = (comprimento * largura) + ((altura * largura) * 2) + ((altura * comprimento) * 2)

# Calculando a quantidade de caixas
caixas = int(area / capacidade)

# Imprimindo.
print "\n== Resultados =="
print "Área total a revestir: %.1f m2" % area
print "Número de caixas: %i" % caixas
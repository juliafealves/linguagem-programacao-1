# coding: utf-8
# Construção de Condomínio
# (C) 2017, Júlia Alves / UFCG Programação 1

# Entrada dos dados
altura = float(raw_input())
base = float(raw_input())
area_casa = float(raw_input())

# Calculando quantidade de casas.
area_terreno = altura * base
casas = int(area_terreno / area_casa)

# Imprimindo quantidade de casas
print "%i casa(s) pode(m) ser construída(s) no terreno." % casas
# coding: utf-8
# Metros em Km
# (C) 2017, Júlia Alves / UFCG Programação 1

# Entrada dos dados
metros = int(raw_input())

# Convertendo metros para Km.
km = metros / 1000.0

# Imprimindo quantidade de casas
print "%i m = %.2f km" % (metros, km)

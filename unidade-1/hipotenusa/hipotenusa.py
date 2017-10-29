# coding: utf-8
# Hipotenusa
# (C) 2017, Júlia Alves / UFCG Programação 1

import math

# Entrada dos dados referente aos catetos.
cateto1 = float(raw_input("Medida do Cateto 1? "))
cateto2 = float(raw_input("Medida do Cateto 2? "))

# Calculando a hipotenusa.
hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)

# Imprimindo o resultado da hipotenusa.
print "Medida da Hipotenusa: %.2f" % hipotenusa
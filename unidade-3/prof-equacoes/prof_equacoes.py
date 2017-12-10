# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Prof Equações - Unidade 3

import math

# Recebe as entradas as raízes reais.
a = float(raw_input())
b = float(raw_input())
c = float(raw_input())

# Calcula o valor de delta.
delta = b ** 2 - (4 * a * c)

# Verifica se o delta é positivo para calcular as raízes.
if delta >= 0:
    x1 = (- b + math.sqrt(delta)) / (2 * a)
    x2 = (- b - math.sqrt(delta)) / (2 * a)

    # Verifica se as raízes são iguais.
    if x1 == x2:
        print "x = %.2f" % x1
    else:
     print "x1 = %.2f" % x1
     print "x2 = %.2f" % x2
else:
    print "sem raizes reais"
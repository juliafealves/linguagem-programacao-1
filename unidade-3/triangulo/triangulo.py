# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: É Triângulo - Unidade 3

# Recebe como entradas os lados do triângulo.
a = float(raw_input())
b = float(raw_input())
c = float(raw_input())

# Verifica se o os lados do triângulo são válidos.
verificando_a = abs(b - c) < a < (b + c)
verificando_b = abs(a - c) < b < (a + c)
verificando_c = abs(a - b) < c < (a + b)

# Caso seja um triângulo calcula o seu perímetro.
if verificando_a or verificando_b or verificando_c:
    perimetro = a + b + c
    print "triangulo valido. %.f" % perimetro
else:
    print "triangulo invalido."
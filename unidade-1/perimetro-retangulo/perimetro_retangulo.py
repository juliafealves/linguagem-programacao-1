# coding: utf-8
# Perímetro do Retângulo
# (C) 2017, Júlia Alves / UFCG Programação 1

# Entrada dos dados referente aos lados.
base = int(raw_input())
altura = int(raw_input())

# Convertendos os dados de milimetro para centimetro.
base = base / 10.0
altura = altura / 10.0

# Calculando o perímetro.
perimetro = 2 * (base + altura)

# Imprimindo o resultado.
print "O perímetro resultante (em cm) é %.2f." % perimetro
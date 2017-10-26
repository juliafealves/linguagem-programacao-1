# coding: utf-8
# Média Ponderada
# (C) 2017 Júlia Alves / UFCG Programação 1

#Entrada dos dados referente as notas.
nota1 = float(raw_input())
nota2 = float(raw_input())
nota3 = float(raw_input())

# Entrada dos dados referente os pesos
peso1 = float(raw_input())
peso2 = float(raw_input())

# Inferindo peso 3
peso3 = 100 - (peso1 + peso2)

# Calculando a média final
mediaFinal = (nota1 * (peso1 / 100)) + (nota2 * (peso2 / 100)) + (nota3 * (peso3 / 100))

# Imprimindo o resultado da média final
print "Média Final: %.1f" % mediaFinal
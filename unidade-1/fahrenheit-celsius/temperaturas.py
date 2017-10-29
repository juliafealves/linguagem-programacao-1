# coding: utf-8
# Fahrenheit Celsius
# (C) 2017, Júlia Alves / UFCG Programação 1

# Entrada de dados referente a temperatura em Fahrenheit
fahrenheit = float(raw_input())

# Calculando Fahrenheit para Celsius
celsius = (fahrenheit - 32) * (5.0 / 9.0)

# Calculando o valor de Kelvin
kelvin = celsius + 273.15

# Imprimindo as temperaturas.
print "Fahrenheit: %.3f F" % fahrenheit
print "Celsius: %.3f C" % celsius
print "Kelvin: %.3f K" % kelvin

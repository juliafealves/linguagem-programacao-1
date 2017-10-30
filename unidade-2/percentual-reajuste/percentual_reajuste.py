# coding: utf-8
# Percentual de Reajuste
# (C) 2017, Júlia Alves / UFCG Programação 1

# Entrada dos dados.
salario_atual = float(raw_input("Valor atual? "))
novo_salario = float(raw_input("Novo valor? "))

# Calculando o percentual de ajuste do salário.
percentual = 100 * (novo_salario - salario_atual) / salario_atual

# Imprimindo.
print "Reajuste de %.1f%%" % percentual
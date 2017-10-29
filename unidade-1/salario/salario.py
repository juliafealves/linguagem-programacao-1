# coding: utf-8
# Salário
# (C) 2017, Júlia Alves / UFCG Programação 1

ir = 0.11
inss = 0.08
sindicato = 0.05

# Entrada dos dados.
salario_bruto = float(raw_input())
horas_trabalho = int(raw_input())

# Calculando a hora bruta
hora_bruta = salario_bruto / horas_trabalho

# Calculando os descontos
desconto_ir = salario_bruto * ir
desconto_inss = salario_bruto * inss
desconto_sindicato = salario_bruto * sindicato

# Calculando o salário líquido
salario_liquido = salario_bruto - (desconto_ir + desconto_inss + desconto_sindicato)

# Calculando a hora líquida
hora_liquida = salario_liquido / horas_trabalho

# Imprimindo as saídas
print "Salário Bruto = " + str(salario_bruto)
print "Hora Bruta = " + str(hora_bruta)
print "Desconto IR = " + str(desconto_ir)
print "Desconto INSS = " + str(desconto_inss)
print "Desconto Sindicato = " + str(desconto_sindicato)
print "Salário Líquido = " + str(salario_liquido)
print "Hora Líquida = " + str(hora_liquida)
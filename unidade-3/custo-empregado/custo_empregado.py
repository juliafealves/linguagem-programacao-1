# coding: utf-8
# Aluno: Júlia Alves
# Matricula: 117211383
# Atividade: Custo Empregado - Unidade 3

# Constante referente aos percentuais de descontos.
PERCENTUAL_VALE_TRANSPORTE = 0.06
PERCENTUAL_FGTS = 0.08
PERCENTUAL_INSS_EMPREGADOR = 0.12

# Entrada dos dados referente ao salário base (R$), dias trabalhados e custo diário com transporte.
salario_base = float(raw_input())
dias_trabalho = int(raw_input())
transporte_dia = float(raw_input())

# Calculando os gastos com transporte.
percentual_transporte = salario_base * PERCENTUAL_VALE_TRANSPORTE
vale_transporte_mes = dias_trabalho * transporte_dia

desconto_transporte = 0
empregador_vale_transporte = 0

if vale_transporte_mes > percentual_transporte:
    desconto_transporte = percentual_transporte
    empregador_vale_transporte = vale_transporte_mes - desconto_transporte

# Verificação da alíquota de desconto do INSS.
aliquota_inss = 0.11

if salario_base <= 1317.07:
    aliquota_inss = 0.08
elif 1317.07 < salario_base <= 2195.12:
    aliquota_inss = 0.09

desconto_inss = salario_base * aliquota_inss

# Calculando o salário líquido.
salario_liquido = salario_base - (desconto_transporte + desconto_inss)

# Custos do empregador
empregador_fgts = salario_base * PERCENTUAL_FGTS
empregador_inss = salario_base * PERCENTUAL_INSS_EMPREGADOR
empregador_custo_total = salario_base + empregador_fgts + empregador_inss + empregador_vale_transporte

# Imprimindo o relatório de gastos com salários.
print "O salário base é R$ %.2f" % salario_base
print "O custo mensal para o empregador é de R$ %.2f" % empregador_custo_total
print "O salário líquido que o trabalhador irá receber no mês é R$ %.2f" % salario_liquido
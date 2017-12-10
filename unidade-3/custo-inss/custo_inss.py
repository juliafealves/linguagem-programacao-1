# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Custo INSS - Unidade 3

# Recebe como entrada o salário.
salario = float(raw_input())

# Valor padrão do percentual do empregado.
percentual_empregado = 0.11

# Verifica o percentual de desconto.
if salario <= 1317.07:
    percentual_empregado = 0.08
elif 1317.08 < salario < 2195.12:
    percentual_empregado = 0.09

# Calcula o INSS do empregador e empregado.
inss_empregado = salario * percentual_empregado
inss_empregador = salario * 0.12

# Exibe os valores de contribuição.
print "O valor da contribuição do INSS a ser pago pelo empregador é de R$ %.2f" % inss_empregador
print "O valor da contribuição do INSS a ser pago pelo empregado é de R$ %.2f" % inss_empregado
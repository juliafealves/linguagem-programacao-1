# coding: utf-8
# Calcula despesas do cinema
# (C) 2017 Júlia Alves / UFCG Programação 1

valor_extra = 2.00

# Entrada dos dados
dia = raw_input("Dia da semana? ")
orcamento = float(raw_input("Orcamento? R$ "))
adultos = int(raw_input("Numero de adultos? "))
criancas = int(raw_input("Numero de criancas? "))
pizza = float(raw_input("Preco da pizza? R$ "))
refrigerante = float(raw_input("Preco do refrigerante? R$ "))
estacionamento = float(raw_input("Preco do estacionamento? R$ "))
cinema = float(raw_input("Preco do ingresso do cinema? R$ "))

# Calculando os gastos
total_pessoas = adultos + criancas
gastos_alimentacao = pizza + refrigerante
gastos_cinema = (cinema * adultos) + ((cinema / 2.00) * criancas) + (total_pessoas * valor_extra)
gastos_total = gastos_cinema + gastos_alimentacao + estacionamento

# Imprimindo os resultados.
print "========== Despesas de " + dia + " =========="
print "Despesas com alimentacao: R$ " + str(gastos_alimentacao)
print "Despesas com cimena: R$ " + str(gastos_cinema)
print "Despesas por pessoa: R$ " + str(gastos_total / total_pessoas)
print "Saldo disponivel: " + str(orcamento - gastos_total)
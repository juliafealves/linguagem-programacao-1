# coding: utf-8
# Aluno: Júlia Alves
# Matricula: 117211383
# Atividade: Transporte Modificado - Unidade 3
import math

preco_tav = 100.00
preco_onibus = 22.00
preco_taxi = 200.00

# Entrada dos dados relacionados a quantidade de passageiros e dinheiro disponível para passagens.
passageiros = int(raw_input())
dinheiro = float(raw_input())

# Calculando os possíveis gastos com transportes.
gasto_tav = passageiros * preco_tav
quantidade_taxis = math.ceil(passageiros / 4.0)
gasto_taxi = quantidade_taxis * preco_taxi
gasto_onibus = passageiros * preco_onibus

# Verifica as opções de transporte em ordem de menor tempo de viagem.
if gasto_tav <= dinheiro:
    print "TAV. R$ %.2f" % gasto_tav
elif gasto_taxi <= dinheiro:
    print "Táxi. R$ %.2f" % gasto_taxi
elif gasto_onibus <= dinheiro:
    print "Ônibus. R$ %.2f" % gasto_onibus
else:
    print "Não é possível realizar a viagem."
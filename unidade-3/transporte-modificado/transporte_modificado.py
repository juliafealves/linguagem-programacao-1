# coding: utf-8
# Aluno: Júlia Alves
# Matricula: 117211383
# Atividade: Transporte Modificado - Unidade 3

preco_tav = 100
preco_onibus = 22
preco_taxi_passageiro = 50
preco_taxi_total = 200

passageiros = int(raw_input())
dinheiro = float(raw_input())

gasto_tav = passageiros *  preco_tav
gasto_taxi = (passageiros / 4.0) * preco_taxi_total
gasto_onibus = passageiros * preco_onibus

if gasto_tav <= dinheiro:
    print "TAV. R$ %.2f" % gasto_tav
elif gasto_taxi <= dinheiro:
    print "Táxi. R$ %.2f" % gasto_taxi
elif gasto_onibus <= dinheiro:
    print "Ônibus. R$ %.2f" % gasto_onibus
else:
    print "Não é possível realizar a viagem."
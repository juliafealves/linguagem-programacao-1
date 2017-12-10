# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Clássico - Unidade 3

# Entradas dos gols Campinense e Treze.
gols_campinense = int(raw_input())
gols_treze = int(raw_input())

# Verifica quem ganhou o clásico.
if gols_campinense > gols_treze:
    print "Campinense"
elif gols_treze > gols_campinense:
    print "Treze"
else:
    print "Empate"
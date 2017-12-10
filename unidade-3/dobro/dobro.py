# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: É Dobro - Unidade 3

# Recebe como entrada os números.
numero1 = float(raw_input())
numero2 = float(raw_input())

# Verifica se algum dos números é o dobro do outro.
if numero1 * 2 == numero2 or numero2 * 2 == numero1:
    print "SIM"
else:
    print "NAO"
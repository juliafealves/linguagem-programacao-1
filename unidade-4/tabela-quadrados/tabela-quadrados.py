# coding: utf-8
# Laboratório de Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Tabela de Quadrados - Unidade 4

inicial = int(raw_input())
final = int(raw_input())

if inicial > final:
    print "---"
else:
    for numero in range(inicial, final + 1):
        print "%i %i" % (numero, numero ** 2)

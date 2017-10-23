# coding: utf-8
# Número de Fatias
# (C) 2017, Júlia Alves / UFCG Programação 1

convidados = int(raw_input())
opcaoInteira = 32 / convidados
opcaoInteiraResto = 32 % convidados
opcaoFloat = 32 / float(convidados)

print 'Opção 1: %d fatias cada, %d de resto' % (opcaoInteira, opcaoInteiraResto)
print 'Opção 2: %.2f fatias cada' % (opcaoFloat)

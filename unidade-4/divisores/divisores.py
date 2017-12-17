# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Divisores - Unidade 4

numero = int(raw_input())

for divisor in range(1, numero):
    if numero % divisor == 0:
        print divisor

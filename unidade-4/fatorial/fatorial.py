# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Fatorial - Unidade 4

numero = int(raw_input())
fatorial = 1

for valor in range(1, numero + 1):
    fatorial *= valor

print fatorial
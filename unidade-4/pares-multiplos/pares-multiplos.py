# coding: utf-8
# Laboratório de Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Pares de Múltiplos - Unidade 4

numeros = raw_input().split()
fator = float(raw_input())
quantidade_pares = 0

pares = []
for i in range(len(numeros) - 1):
    numero = float(numeros[i])
    vizinho = float(numeros[i + 1])

    if vizinho / numero == fator or numero / vizinho == fator:
        quantidade_pares += 1
        pares.append(numero)
        pares.append(vizinho)

print "%i par(es)" % quantidade_pares

for i in range(0, len(pares), 2):
    print "%.0f %.0f" % (pares[i], pares[i + 1])

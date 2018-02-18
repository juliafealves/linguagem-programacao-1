# coding: utf-8
# Laboratório de Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: B2 para B10 - Unidade 4

binario = raw_input()
decimal = 0
posicao = 0

for indice in range(len(binario) - 1, -1, -1):
    bit = int(binario[posicao])
    potenciacao = 2 ** indice
    valor = bit * potenciacao
    decimal += valor
    posicao += 1

    print "%i * %i = %i" % (bit, potenciacao, valor)

print "%s(2) = %i(10)" % (binario, decimal)
# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Conta Divisíveis - Unidade 4

# Entrada dos dados referente ao valor a ser considerado divísivel e a quantidade de entradas a serem coletadas.
divisivel = int(raw_input())
quantidade_numeros = int(raw_input())

total_divisiveis = 0

# Coleta os números inteiros e verifica se é divisível pelo valor anteriormente informado.
for quantidade in range(quantidade_numeros):
    numero = int(raw_input())

    if numero % divisivel == 0:
        total_divisiveis += 1

# Calcula o percentual de números divisíveis existentes.
percentual = 100.0 * total_divisiveis / quantidade_numeros

print "%i (%.1f%%)" % (total_divisiveis, percentual)

# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Pedágio - Unidade 3

transporte = raw_input()
valor = 0

# Verifica o tipo de pedágio de acordo com o transporte.
if transporte ==  "Automóvel utilitário" or transporte == "Ônibus":
    valor = 11.4
elif transporte == "Caminhão":
    valor = 9.6
elif transporte == "Motocicleta":
    valor = 5.7

# Coleta o eixo e calcula o pedágio.
if transporte == "Ônibus" or transporte == "Caminhão":
    eixo = int(raw_input())
    valor *= eixo

# Imprime o valor do pedágio, quando existir.
if valor == 0:
    print "Veículo não cadastrado."
else:
    print "Valor a pagar: R$ %.2f." % valor
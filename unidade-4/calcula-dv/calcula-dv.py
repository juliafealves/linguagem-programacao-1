# coding: utf-8
# Laboratório de Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Calcula DV - Unidade 4

numero_banco = raw_input()

posicao_par = 0
posicao_impar = 0

for indice in range(len(numero_banco)):
    numero = int(numero_banco[indice])

    if indice % 2 == 0:
        posicao_par += numero
    else:
        posicao_impar += numero

digito_verificador = (posicao_par * posicao_impar) % 11

if digito_verificador == 10:
    numero_banco += "-X"
else:
    numero_banco += "-" + str(digito_verificador)

print numero_banco
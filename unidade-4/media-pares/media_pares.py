# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Média dos Pares - Unidade 4

# Recebe como entrada a quantidade de números a serem lidos.
# Deve ser maior um número inteiro maior que 0.
quantidade_entradas = int(raw_input())

quantidade_pares = 0
soma_pares = 0
numeros = []

# Coleta os números inteiros da entrada.
for entrada in range(quantidade_entradas):
    numero = int(raw_input())

    # Verifica se o número é par.
    if numero % 2 == 0:
        soma_pares += numero
        quantidade_pares += 1.0

    numeros.append(numero)

# Calcula média aritmética dos números pares.
media_pares = soma_pares / quantidade_pares

quantidade_menor_media = 0

# Conta quantidade de números menores que a média.
for numero in numeros:
    if numero < media_pares:
        quantidade_menor_media += 1

print "soma: %i" % soma_pares
print "média: %.1f" % media_pares
print "%i número(s) abaixo da média" % quantidade_menor_media
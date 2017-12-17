# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Média dos Extremos - Unidade 4

# Recebe como entrada a quantidade de números a serem lidos.
# Deve ser maior um número inteiro maior que 0.
quantidade_entradas = int(raw_input())

numeros = []
maior = 0
menor = 0

# Coleta os números inteiros da entrada.
for entrada in range(quantidade_entradas):
    numero = int(raw_input())

    # Verifica qual o maior e menor número.
    if entrada == 0:
        maior = numero
        menor = numero
    elif numero < menor:
        menor = numero
    elif numero > maior:
        maior = numero

    numeros.append(numero)

# Calcula média aritmética dos extremos.
media = (maior + menor) / 2.0

quantidade_acima_media = 0
quantidade_abaixo_media = 0

# Conta quantidade de números menores e maiores que a média.
for numero in numeros:
    if numero > media:
        quantidade_acima_media += 1
    elif numero < media:
        quantidade_abaixo_media += 1

print "Menor número: %i" % menor
print "Maior número: %i" % maior
print "Média dos extremos: %.2f" % media
print "%i número(s) abaixo da média" % quantidade_abaixo_media
print "%i número(s) acima da média" % quantidade_acima_media
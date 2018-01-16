# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Herão - Unidade 4

import math

# Constante referente o valor mínimo para ser um triângulo grande.
MAIOR_AREA = 100

# Recebe a quantidade de triângulos a serem lidos.
quantidade_triangulos = int(raw_input())


quantidade_maiores = 0
areas_maiores = 0
area_media = 0

for n in range(1, quantidade_triangulos + 1):
    # Separa as entradas referente aos lados do triângulo.
    lados = raw_input().split()
    a = float(lados[0])
    b = float(lados[1])
    c = float(lados[2])

    # Calcula o semiperímetro do triângulo.
    semiperimetro = (a + b + c) / 2

    # Calcula o teorema de Herão.
    area = math.sqrt(semiperimetro * (semiperimetro - a) * (semiperimetro - b) * (semiperimetro - c))

    print "Área %i: %.2f" % (n, area)

    # Verifica se a área do triângulo atende o quesito de maior triângulo.
    if area > MAIOR_AREA:
        quantidade_maiores += 1
        areas_maiores += area

# Caso existam triângulos maiores será impressa a quantidade e as áreas médias.
if quantidade_maiores > 0:
    # Calcula a área média dos triângulos maiores.
    area_media = areas_maiores / quantidade_maiores

    print "Número maiores: %i, área média: %.2f" % (quantidade_maiores, area_media)

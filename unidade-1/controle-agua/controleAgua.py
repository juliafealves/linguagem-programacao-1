# coding: utf-8
# Controle de Água
# (C) 2017 Júlia Alves / UFCG Programação 1
import math

velocidadeVazao = float(raw_input())
diametroCano = float(raw_input())
tempo = int(raw_input())

# Calculando a quantidade de água
seccao = (math.pi * diametroCano ** 2) / 4
vazao = velocidadeVazao * seccao * 1000
totalAgua = tempo * vazao

# Imprimindo resultado
print 'Quantidade de água = %f litros.' % totalAgua

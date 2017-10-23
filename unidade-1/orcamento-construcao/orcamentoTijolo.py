# coding: utf-8
# Orçamento Construção
# (C) 2017 Júlia Alves / UFCG Programação 1
import math

# Coletando os dados de entrada
precoTijolo = float(raw_input('Digite o preço da unidade do tijolo (Em reais): '))
alturaTijolo = float(raw_input('Digite a altura do tijolo (Em metros): '))
larguraTijolo = float(raw_input('Digite o comprimento do tijolo (Em metros): '))
alturaParede = float(raw_input('Digite a altura das paredes (Em metros): '))
larguraParede = float(raw_input('Digite o comprimento das paredes (Em metros): '))

# Calculando a quantidade de tijolos
totalTijolos = (alturaParede / alturaTijolo) * (larguraParede / larguraTijolo)

# Calculando o orçamento
orcamentoTotal = math.ceil(totalTijolos) * precoTijolo

# Exibindo os resultados
print 'O número total de tijolos é %.1f e o orçamento final é de R$ %.1f' % (totalTijolos, orcamentoTotal)

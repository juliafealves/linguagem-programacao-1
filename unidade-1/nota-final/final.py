# coding: utf-8
# Nota na Final
# (C) 2017 Júlia Alves / UFCG Programação 1

# Colentando a entrada das notas dos estágios
print '== Estágio 1 =='
peso1 = float(raw_input('Peso? '))
nota1 = float(raw_input('Nota? '))

print '== Estágio 2 =='
peso2 = float(raw_input('Peso? '))
nota2 = float(raw_input('Nota? '))

print '== Estágio 3 =='
peso3 = float(raw_input('Peso? '))
nota3 = float(raw_input('Nota? '))

# Calculando a média parcial
mediaParcial = ((peso1 * nota1) + (peso2 * nota2) + (peso3 * nota3))

# Fatores para final
fator6 = 0.6
fator4 = 0.4

# Calculando a nota final para média 5.
finalMedia5 = (5.0 - (mediaParcial * fator6)) / fator4

# Calculando a nota final para média 7.
finalMedia7 = (7.0 - (mediaParcial * fator6)) / fator4

# Imprimindo os resultados
print '== Resultados =='
print 'Média parcial: %.1f' % mediaParcial
print 'Nota na final, pra média 5.0 = %.1f' % finalMedia5
print 'Nota na final, pra média 7.0 = %.1f' % finalMedia7

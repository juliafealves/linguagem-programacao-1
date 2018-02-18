# coding: utf-8
# Laboratório de Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Salário Mínimo (US$ 100) - Unidade 4

ano_inicial = int(raw_input())
ano_final = int(raw_input())

anos = ano_final - ano_inicial + 1

anos_acima = 0
salarios_acima = 0

anos_abaixo = 0
salarios_abaixo = 0

for ano in range(anos):
    salario = float(raw_input())

    if salario > 100:
        anos_acima += 1
        salarios_acima += salario
    else:
        anos_abaixo += 1
        salarios_abaixo += salario

percentual_abaixo = (100.0 * anos_abaixo) / anos
print "%i ano(s) abaixo (%.0f%% dos anos)" % (anos_abaixo, percentual_abaixo)

if anos_abaixo > 0:
    media_abaixo = salarios_abaixo / anos_abaixo
    print "média dos anos abaixo: U$ %.2f" % media_abaixo

percentual_acima = (100.0 * anos_acima) / anos
print "%i ano(s) acima (%.0f%% dos anos)" % (anos_acima, percentual_acima)

if anos_acima > 0:
    media_acima = salarios_acima / anos_acima
    print "média dos anos acima: U$ %.2f" % media_acima




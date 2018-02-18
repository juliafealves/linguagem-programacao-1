# coding: utf-8
# Laboratório de Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Lucro Mensal - Unidade 4

meses = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]

for entrada in range(12):
    dados = raw_input().split(" ")
    receita = float(dados[0])
    despesa = float(dados[1])
    lucro = receita - despesa

    print "%s %4.1f" % (meses[entrada], lucro)

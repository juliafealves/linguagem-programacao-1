# coding: utf-8
# Aprovação Unidades
# (C) 2017, Júlia Alves / UFCG Programação 1

# Entrada dos dados
unidade = int(raw_input("Unidade? "))
media = float(raw_input("Média de aprovação na unidade? "))

# Calculando a próxima unidade.
proxima_unidade = unidade + 1

# Imprimindo o resultado.
print "\nO aluno vai para a unidade %i com média %.1f." % (proxima_unidade, media)
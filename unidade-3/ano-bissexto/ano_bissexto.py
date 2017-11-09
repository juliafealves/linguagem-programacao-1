# coding: utf-8
# Aluno: Júlia Alves
# Matricula: 117211383
# Atividade: Ano Bissexto - Unidade 3

ano = int(raw_input())
mensagem = "não é bissexto"

# Verifica se o ano é bissexto.
if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    mensagem = "é bissexto"

print "%i %s" % (ano, mensagem)
# coding: utf-8
# Aluno: Júlia Alves
# Matricula: 117211383
# Atividade: Mais velho - Unidade 3

# Entrada dos dados de duas pessoas (nome e dia, mês e ano).
nome_pessoa1 = raw_input()
dia_pessoa1 = int(raw_input())
mes_pessoa1 = int(raw_input())
ano_pessoa1 = int(raw_input())

nome_pessoa2 = raw_input()
dia_pessoa2 = int(raw_input())
mes_pessoa2 = int(raw_input())
ano_pessoa2 = int(raw_input())

mais_velha = nome_pessoa1

# Verifica a pessoa mais velha.
if (ano_pessoa2 < ano_pessoa1) or (ano_pessoa2 == ano_pessoa1 and mes_pessoa2 < mes_pessoa1) or (ano_pessoa2 == ano_pessoa1 and mes_pessoa2 == mes_pessoa1 and dia_pessoa2 < dia_pessoa1):
    mais_velha = nome_pessoa2
elif ano_pessoa2 == ano_pessoa1 and mes_pessoa2 == mes_pessoa1 and dia_pessoa2 == dia_pessoa1:
    mais_velha = "nenhuma"

print mais_velha
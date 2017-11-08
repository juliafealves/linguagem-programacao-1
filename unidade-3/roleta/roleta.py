# coding: utf-8
# Aluno: Júlia Alves
# Matricula: 117211383
# Atividade: Roleta - Unidade 3

numero = int(raw_input())
cor = raw_input()

numero_sorteado = int(raw_input())
cor_sorteada = raw_input()

pontuacao = 0

if numero == numero_sorteado and cor == cor_sorteada:
    pontuacao = 150
elif numero == numero_sorteado and cor != cor_sorteada:
    pontuacao = 100
elif numero != numero_sorteado and cor == cor_sorteada:
    pontuacao = 50

    if numero_sorteado > numero:
        pontuacao += 30
    else:
        pontuacao += 50

print pontuacao

# coding: utf-8
# Laboratório de Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Árvore de Natal - Unidade 4

altura = int(raw_input())

espacos = altura - 1
tronco = " " * espacos + "o"

for camada in range(1, altura * 2, 2):
    margem = " " * espacos
    folhas = "o" * camada

    print margem + folhas
    espacos -= 1

print tronco

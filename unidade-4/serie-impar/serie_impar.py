# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Série (ímpare 1) - Unidade 4

# Imprime o números ímpares de 1 a 101.
# Quando divisível por 3 ou 5, substitui por *.
for numero in range(1, 102, 2):
    if numero % 3 == 0 or numero % 5 == 0:
        print "*"
    else:
        print numero
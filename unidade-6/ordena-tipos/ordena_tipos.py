# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Ordena Tipos - Unidade 6

# Retorna uma lista com tipos ordenados 
# (números inteiros, letras, outros tipos).
def ordena_tipos(lista):
    inteiros = []
    letras = []
    outros = []

    for elemento in lista:
        if elemento.isdigit():
            inteiros.append(elemento)
        elif elemento.isalpha():
            letras.append(elemento)
        else:
            outros.append(elemento)

    return inteiros + letras + outros
# coding: utf-8
# Laboratório de Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Primeira Vogal - Unidade 4

palavra = raw_input()

vogais = ["a", "e", "i", "o", "u"]
encontrada = False

for letra in palavra:
    letra_minuscula = letra.lower()

    if letra_minuscula in vogais and not encontrada:
        encontrada = True
        print letra

if not encontrada:
    print "-"

# coding: utf-8
# Laboratório de Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Espaço por Vírgula - Unidade 4

frase = raw_input()
inicio = int(raw_input())
fim = int(raw_input())

nova_frase = ""

for indice in range(inicio, fim):
    letra = frase[indice]

    # Se for um espaço em branco substituir na nova frase por vírgula.
    if letra == " ":
        nova_frase += ","
    else:
        nova_frase += letra

    # Adiciona espaço em branco somente se não for a última letra.
    if indice != fim - 1:
        nova_frase += " "

print nova_frase

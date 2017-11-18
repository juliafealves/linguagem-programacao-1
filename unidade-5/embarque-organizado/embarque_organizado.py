# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Embarque Organizado - Unidade 5

# Recebe uma sequência de números inteiros separados por espaço.
poltronas = raw_input()

# Separa a entrada dos dados referente ao número da poltrona.
poltronas = poltronas.split()

tamanho = len(poltronas)
indice = 0
impar = 0
par = tamanho - 1

mensagem = "ok"

# Verdadeiro enquanto o índice for menor que o tamanho da lista.
while indice < tamanho:
    if poltronas[indice] != "":
        if int(poltronas[indice]) % 2 != 0:
            impar = indice
        else:
            par = indice

    # Verifica se existe um valor par antes do valor ímpar através do índice.
    if par < impar:
        mensagem = "erro"
        break

    indice += 1

print mensagem

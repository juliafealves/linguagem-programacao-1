# coding: utf-8
# Laboratório de Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Ordem Alfabética - Unidade 4

# Recebe o quantitativo de palavras chaves.
quantidade_palavras = int(raw_input())

palavras = []

# Recebe e guarda as palavras informadas.
for n in range(quantidade_palavras):
    palavra = raw_input()
    palavras.append(palavra)

print "---"

# Recebe a palavra-chave a ser comparada.
palavra_chave = raw_input()

palavras_antes = 0
palavras_depois = 0

# Compara as palavras com a palavra-chave e contabiliza as palavras antes e depois.
# Evitando quantificar a palavra-chave em questão.
for palavra in palavras:
    if palavra > palavra_chave:
        palavras_depois += 1
    elif palavra < palavra_chave:
        palavras_antes += 1

print "%i antes" % palavras_antes
print "%i depois" % palavras_depois
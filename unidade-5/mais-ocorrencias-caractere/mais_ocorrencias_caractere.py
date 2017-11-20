# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Mais Ocorrências Caractere - Unidade 5

# Recebe uma entrada inicial.
entrada = raw_input()
palavras = []

# Recebe todas as entradas possíveis enquanto não digitar a palavra "fim"
while entrada != "fim":
    palavras.append(entrada)
    entrada = raw_input()

# Entradas referentes ao caracter escolhido para busca e quantidade mínima de ocorrência deste caracter.
caracter_escolhido = raw_input()
ocorrencia_minima = int(raw_input())

# Variável para verificar se encontrou alguma palavra.
palavra_encontrada = 0

# Busca o caracterer em todas as palavras e verifica se atende as quantidade mínima de ocorrência.
for palavra in palavras:
    quantidade_ocorrencia = 0

    for caracter in palavra:
        if caracter == caracter_escolhido:
            quantidade_ocorrencia += 1
    
    if quantidade_ocorrencia > ocorrencia_minima:
        palavra_encontrada += 1
        print palavra

# Verifica se nenhuma palavra foi encontrada.
if palavra_encontrada == 0:
    print "Nenhuma palavra encontrada."
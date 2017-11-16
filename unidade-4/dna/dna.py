# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: DNA - Unidade 4

# Recebe a entrada duas sequências de moléculas de DNA.
sequencia_dna1 = raw_input()
sequencia_dna2 = raw_input()

nucleotideos_iguais = 0
semelhantes = "nao"

# Verifica se são de mesmo tamanho e quantifica os nucleotídeos que estão na mesma posição e são iguais.
if len(sequencia_dna1) == len(sequencia_dna2):
    for indice in range(len(sequencia_dna1)):
        if sequencia_dna1[indice] == sequencia_dna2[indice]:
            nucleotideos_iguais += 1

# Verifica se a quantidade de nucleotídeos é maior que a metade do tamanho da cadeia.
if nucleotideos_iguais > (len(sequencia_dna1)/2):
    semelhantes = "sim"

print semelhantes


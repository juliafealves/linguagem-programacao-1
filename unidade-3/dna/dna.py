# coding: utf-8
# Aluno: Júlia Alves
# Matricula: 117211383
# Atividade: Tamanho DNA - Unidade 3

# Recebe as sequência de DNA: adenina (A), guanina(G), citosina(C) e timina (T)
sequencia_dna1 = raw_input()
sequencia_dna2 = raw_input()
sequencia_dna3 = raw_input()

# Coleta os tamanhos de cada sequência, a fim de facilitar as comparações.
tamanho_dna1 = len(sequencia_dna1)
tamanho_dna2 = len(sequencia_dna2)
tamanho_dna3 = len(sequencia_dna3)

# Verifica a menor sequência de DNA e em caso de empate, a primeira a ser dada como entrada.
if tamanho_dna1 == tamanho_dna2 or tamanho_dna1 == tamanho_dna3:
    menor_dna = sequencia_dna1
elif tamanho_dna2 == tamanho_dna3:
    menor_dna = sequencia_dna2
elif tamanho_dna1 < tamanho_dna2 and tamanho_dna1 < tamanho_dna3:
    menor_dna = sequencia_dna1
elif tamanho_dna2 < tamanho_dna1 and tamanho_dna2 < tamanho_dna3:
    menor_dna = sequencia_dna2
elif tamanho_dna3 < tamanho_dna1 and tamanho_dna3 < tamanho_dna2:
    menor_dna = sequencia_dna3

# Imprime a menor sequência de DNA.
print "%s %i" % (menor_dna, len(menor_dna))

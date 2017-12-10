# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Concurso - Unidade 3

# Recebe como entrada as notas e idade do candidato 1.
candidato1_escrita = float(raw_input())
candidato1_didatica = float(raw_input())
candidato1_titulacao = float(raw_input())
candidato1_idade = int(raw_input())

# Recebe como entrada as notas e idade do candidato 2.
candidato2_escrita = float(raw_input())
candidato2_didatica = float(raw_input())
candidato2_titulacao = float(raw_input())
candidato2_idade = int(raw_input())

# Calcula a nota final dos candidatos 1 e 2.
candidato1_nota_final = candidato1_escrita * 0.3 + candidato1_didatica * 0.4 + candidato1_titulacao * 0.3
candidato2_nota_final = candidato2_escrita * 0.3 + candidato2_didatica * 0.4 + candidato2_titulacao * 0.3

# Verifica o candidato aprovado.
if candidato1_nota_final == candidato2_nota_final:
    if candidato1_idade > candidato2_idade:
        print "O primeiro candidato foi aprovado com média %.1f." % candidato1_nota_final
    elif candidato1_idade < candidato2_idade:
        print "O segundo candidato foi aprovado com média %.1f." % candidato2_nota_final
    else:
        print "Empate."
else:
    if candidato1_nota_final > candidato2_nota_final:
        print "O primeiro candidato foi aprovado com média %.1f." % candidato1_nota_final
    else:
        print "O segundo candidato foi aprovado com média %.1f." % candidato2_nota_final
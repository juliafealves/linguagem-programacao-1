# coding: utf-8
# Percentagem de Aprovados
# (C) 2017, Júlia Alves / UFCG Programação 1

print "Análise da Turma\n==="

# Entrada dos dados
alunos_aprovados = int(raw_input("Número de aprovados? "))
alunos_reprovados = int(raw_input("Número de reprovados? "))

# Calculando as percentagens.
total_alunos = alunos_aprovados + alunos_reprovados
percentagem_aprovados = (100.0 * alunos_aprovados) / total_alunos
percetagem_reprovados = (100.0 * alunos_reprovados) / total_alunos

# Imprimindo os resultados.
print "---\nTotal de alunos na turma: %i" % total_alunos
print "Aprovados: %i = %.1f%%" % (alunos_aprovados, percentagem_aprovados)
print "Reprovados: %i = %.1f%%" % (alunos_reprovados, percetagem_reprovados)

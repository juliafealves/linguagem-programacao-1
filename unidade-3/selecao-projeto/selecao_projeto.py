# coding: utf-8
# Aluno: Júlia Alves
# Matricula: 117211383
# Atividade: Seleção Projeto - Unidade 3

CRE_MINIMO = 7
EXPERIENCIA_MINIMA = 6

# Entrada das informação de CRE, Experiência e nota em entrevista.
cre = float(raw_input())
experiencia = float(raw_input())
nota_entrevista = float(raw_input())

# Verifica a classificação do aluno.
if cre < CRE_MINIMO and experiencia < EXPERIENCIA_MINIMA:
    mensagem = "Candidato eliminado. CRE e experiência abaixo do limite."
elif cre < CRE_MINIMO:
    mensagem = "Candidato eliminado. CRE abaixo do limite."
elif experiencia < EXPERIENCIA_MINIMA:
    mensagem = "Candidato eliminado. Experiência abaixo do limite."
else:
    if nota_entrevista <= 3:
        mensagem = "Candidato classificado."
    else:
        mensagem = "Candidato aprovado."

print mensagem
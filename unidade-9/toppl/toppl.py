# coding: utf-8
# Laboratório de Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Toppl - Unidade 9


# Verifica se o aluno fez a inscrição.
def verificar_inscrito(aluno, inscritos):
    for inscrito in inscritos:
        if aluno == inscrito:
            return True

    return False


# Retorna a quantidade de alunos eliminado nos critérios de média de corte e não inscrito.
def filtra_alunos(alunos, inscritos, media_corte):
    removidos = 0

    for i in range(len(alunos) -1, -1, -1):
        aluno = alunos[i]

        if not verificar_inscrito(aluno[0], inscritos) or aluno[1] < media_corte:
            alunos.pop(i)
            removidos += 1

    return removidos
# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Status - Unidade 3

# Recebe as 3 notas do aluno e a quantidade de faltas.
nota1 = float(raw_input())
nota2 = float(raw_input())
nota3 = float(raw_input())
faltas = int(raw_input())

# Calculando a média
frequencia = (30.0 - faltas) / 30.0

# Verifica a situação do aluno pela frequência.
if frequencia > 0.75:
    # Calcula a média aritmética do aluno.
    media = (nota1 + nota2 + nota3) / 3

    # Verifica a situação do aluno pela média.
    if media >= 7:
        mensagem = "aprovado por media"
    elif 4 <= media < 7:
        mensagem = "prova final"
    else:
        mensagem = "reprovado por nota"
else:
    mensagem = "reprovado por faltas"

print mensagem
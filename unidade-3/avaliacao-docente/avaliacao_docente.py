# coding: utf-8
# Aluno: Júlia Alves
# Matricula: 117211383
# Atividade: Avaliação Docente - Unidade 3

# Constantes para melhor parametrização do programa.
MEDIA_MINIMA = 140
QUANTIDADE_MINIMA_SEMESTRE = 4
PONTOS_MINIMOS_ENSINO = 320
PONTOS_MINIMOS_INTELECTUAL = 100
PONTOS_MINIMOS_ORIENTACAO = 20

# Entrada dos dados referente a quantidade de semestres e pontuações do docente.
quantidade_semestre = int(raw_input())
pontuacao_ensino = float(raw_input())
pontuacao_intelectual = float(raw_input())
pontuacao_orientacao = float(raw_input())
pontuacao_administrativa = float(raw_input())

# Calculando a média do docente.
total_pontos = (pontuacao_ensino + pontuacao_intelectual + pontuacao_orientacao + pontuacao_administrativa) / 4

mensagem = "Promoção deferida. Parabéns!"

# Verificando se docente apto para promoção.
if quantidade_semestre < QUANTIDADE_MINIMA_SEMESTRE:
    mensagem = "Promoção indeferida. Número de semestres insuficiente."
elif pontuacao_ensino < PONTOS_MINIMOS_ENSINO or pontuacao_intelectual < PONTOS_MINIMOS_INTELECTUAL or pontuacao_orientacao < PONTOS_MINIMOS_ORIENTACAO:
    mensagem = "Promoção indeferida. Pontuação mínima não alcançada."
elif total_pontos < MEDIA_MINIMA:
    mensagem = "Promoção indeferida. Média insuficiente."

print mensagem

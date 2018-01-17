# coding: utf-8
# Laboratório de Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: SAMU - Unidade 4

atendimentos = []
total_atendimentos = 0

# Recebe e guarda os atendimentos do SAMU durante os 12 meses.
for n in range(12):
    atendimento = int(raw_input())
    atendimentos.append(atendimento)

    # Contabiliza os atendimentos realizados.
    total_atendimentos += atendimento


# Calcula a média de atendimentos realizados.
media = total_atendimentos / 12.0

print "Média mensal de atendimentos: %.2f\n----" % media

# Verifica e imprime os meses com atendimentos acima da média.
for indice in range(len(atendimentos)):
    if atendimentos[indice] > media:
        print "Mês %i: %i" % (indice + 1, atendimentos[indice])

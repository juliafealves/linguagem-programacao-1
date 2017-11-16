# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Autorização Voos - Unidade 4

# Entrada dos dados tempo disponível e quantidade de voos.
tempo_disponivel = int(raw_input())
avioes = int(raw_input())

voos_autorizados = 0

# Contabiliza os voos autorizados e verifica se existe tempo hábil para executar a decolagem.
for quantidade in range(avioes):
    tempo_voo = int(raw_input())

    if tempo_disponivel >= tempo_voo:
        voos_autorizados += 1
        tempo_disponivel -= tempo_voo
    elif tempo_disponivel <= 0:
        break

# Imprime os voos autorizados.
print "%i voo(s) autorizados." % voos_autorizados
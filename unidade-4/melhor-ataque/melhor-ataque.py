# coding: utf-8
# Laboratório de Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Melhor Ataque - Unidade 4

melhores_times = []

# Inicializa a quantidade de times, no mínimo deve ter 2.
quantidade_times = int(raw_input())

# Considera o primeiro dado como o melhor time e ataque.
melhor_time = raw_input()
melhores_times.append(melhor_time)
melhor_ataque = int(raw_input())

total_gols = melhor_ataque

for n in range(1, quantidade_times):
    time = raw_input()
    ataque = int(raw_input())

    # Compara os ataques dos times, caso seja
    # igual ao melhor_time adiciona na lista, caso
    # seja maior limpa a lista e adiciona.
    if melhor_ataque == ataque:
        melhores_times.append(time)
    elif melhor_ataque < ataque:
        melhores_times = []
        melhor_ataque = ataque
        melhor_time = time

        melhores_times.append(time)

    total_gols += ataque

# Calcula a média de gols dos times.
media_gols = total_gols / float(quantidade_times)

# Imprime o(s) time(s) com melhor(es) ataque(s) e a média de gols.
print "Time(s) com melhor ataque (%i gol(s)):" % melhor_ataque

for time in melhores_times:
    print time

print "\nMédia de gols marcados: %.1f" % media_gols
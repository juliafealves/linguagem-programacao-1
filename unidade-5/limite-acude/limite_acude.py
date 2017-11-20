# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Limite Açude - Unidade 5

limite_superior = float(raw_input())
nivel = float(raw_input())

while nivel < limite_superior:
    operacao = raw_input()
    operacao = operacao.split()

    if operacao[0] == "demanda":
        nivel -= float(operacao[1])
    else:
        nivel += float(operacao[1])

print "Açude passou a liberar água."
print "Nível: %.2f" % nivel
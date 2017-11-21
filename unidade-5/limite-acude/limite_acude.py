# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Limite Açude - Unidade 5

# Recebe as entradas referente ao limite superior do açude e o nível atual do açude.
limite_superior = float(raw_input())
nivel = float(raw_input())

# Enquanto não atingir o limite superior do açude será realizada operações no açude.
while nivel < limite_superior:
    operacao = raw_input()
    operacao = operacao.split()

    # Caso a operação seja "demanda" será subtraído água do açude. Caso contrário, adicionará nível no açude.
    if operacao[0] == "demanda":
        nivel -= float(operacao[1])

        # Caso o nível seja abaixo de 0, deve-se setar o nível para positivo.
        if nivel < 0:
            nivel = 0.0
    else:
        nivel += float(operacao[1])

# Imprime o nível do açude e informe sobre a liberação de água.
print "Açude passou a liberar água."
print "Nível: %.2f" % nivel

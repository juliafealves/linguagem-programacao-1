# coding: utf-8
# Laboratório de Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Converte Senha - Unidade 4

senha = raw_input()

nova_senha = senha[0]
trocas = 0

for i in range(1, len(senha)):
    letra = senha[i].lower()

    if letra == "a":
        nova_senha += "4"
        trocas += 1
    elif letra == "e":
        nova_senha += "3"
        trocas += 1
    elif letra == "i":
        nova_senha += "1"
        trocas += 1
    elif letra == "o":
        nova_senha += "0"
        trocas += 1
    else:
        nova_senha += senha[i]

print "%s (%i troca(s))" % (nova_senha, trocas)
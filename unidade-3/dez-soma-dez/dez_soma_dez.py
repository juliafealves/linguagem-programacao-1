# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Dez ou Soma Dez - Unidade 3

# Recebe os números inteiros como entrada.
numero1 = int(raw_input())
numero2 = int(raw_input())

# Verifica se um dos números é 10.
if numero1 == 10 or numero2 == 10:
    print "SIM"
else:
    # Caso contrário realiza a soma e verifica o resultado.
    soma = numero1 + numero2

    if soma == 10:
        print "SIM"
    else:
        print "NAO"

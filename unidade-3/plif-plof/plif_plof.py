# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Plif Plof - Unidade 3

# Recebe os números inteiros como entrada.
numero1 = int(raw_input())
numero2 = int(raw_input())
numero3 = int(raw_input())

# Calcula o somatório dos números
somatorio = numero1 + numero2 + numero3

# Verifica se o somatório é divisível por 3 ou 5.
if somatorio % 3 == 0 and somatorio % 5 == 0:
    print "plifplof"
elif somatorio % 3 == 0:
    print "plif"
elif somatorio % 5 == 0:
    print "plof"
else:
    print somatorio
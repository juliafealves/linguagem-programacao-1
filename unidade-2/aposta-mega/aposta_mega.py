# coding: utf-8
# Aposta da Mega Tripla
# (C) 2017, Júlia Alves / UFCG Programação 1

# Entrada dos dados.
numero1 = int(raw_input())
numero2 = int(raw_input())
numero3 = int(raw_input())

# Gerando os valores.
numero1 = numero1 % 11
numero2 = numero2 % 11
numero3 = numero3 % 11

# Imprimindo.
print "%02i-%02i-%02i" % (numero1, numero2, numero3)
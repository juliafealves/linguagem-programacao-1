# coding: utf-8
# Espaço em Disco Simplificado
# (C) 2017, Júlia Alves / UFCG Programação 1

# Entrada dos dados referente os espaços.
usuario1 = raw_input()
espaco1 = int(raw_input())

usuario2 = raw_input()
espaco2 = int(raw_input())

usuario3 = raw_input()
espaco3 = int(raw_input())

# Convertendo os dados para MB.
espaco1 = (espaco1 / 1024.0) / 1024.0
espaco2 = (espaco2 / 1024.0) / 1024.0
espaco3 = (espaco3 / 1024.0) / 1024.0

# Calculando o total e média de espaço.
total = espaco1 + espaco2 + espaco3
media = total / 3.0

# Imprimindo os espaços.
print "SPLab - Espaço utilizado pelos usuários"
print "---------------------------------------------"
print "Nr., Usuário, Espaço Utilizado\n"
print "1, %s, %.2f MB" % (usuario1, espaco1)
print "2, %s, %.2f MB" % (usuario2, espaco2)
print "3, %s, %.2f MB" % (usuario3, espaco3)
print "\nEspaço total ocupado: %.2f MB" % total
print "Espaço médio ocupado: %.2f MB" % media
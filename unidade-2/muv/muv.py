# coding: utf-8
# Movimento Uniformemente Variado
# (C) 2017, Júlia Alves / UFCG Programação 1

# Entrada dos dados
posicao_inicial = float(raw_input("Posição inicial? "))
velocidade_inicial = float(raw_input("Velocidade inicial? "))
tempo_deslocamento = float(raw_input("Tempo? "))
aceleracao = float(raw_input("Aceleração? "))

# Calculando velocidade final
velocidade_final = velocidade_inicial + (aceleracao * tempo_deslocamento)

# Calculando velocidade média
velocidade_media = velocidade_inicial + (aceleracao * tempo_deslocamento) / 2

# Calulando posição final
posicao_final = posicao_inicial + (velocidade_inicial * tempo_deslocamento) + (aceleracao * (tempo_deslocamento ** 2)) / 2

# Imprimindo o valor das passagens e forma de pagamento
print "\nDados da questão\n================"
print "   Posição inicial: %.2f m" % posicao_inicial
print "Velocidade inicial: %.2f m/s" % velocidade_inicial
print "        Aceleração: %.2f m/s2" % aceleracao
print "             Tempo: %.2f s" % tempo_deslocamento
print "  Velocidade final: %.2f m/s" % velocidade_final
print "  Velocidade média: %.2f m/s" % velocidade_media
print "     Posição final: %.2f m" % posicao_final

# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Ciclo Trig - Unidade 3

# Entrada dos dados referente aos graus.
angulo = float(raw_input())

# Verificar se deu a volta no ciclo.
if angulo > 360:
	angulo = angulo % 360

# Verificando os quadrantes.
if 0 < angulo < 90:
    print "Quadrante 1"
elif 90 < angulo < 180:
	print "Quadrante 2"
elif 180 < angulo < 270:
    print "Quadrante 3"
elif 270 < angulo < 360:
    print "Quadrante 4"
else:
    print "Sobre eixos"
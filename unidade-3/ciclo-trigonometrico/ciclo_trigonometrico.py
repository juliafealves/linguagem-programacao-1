# coding: utf-8
# Aluno: Júlia Alves
# Matricula: 117211383
# Atividade: Ciclo Trigonométrico

angulo_total = 360.0

# Entrada dos dados referente aos graus.
angulo = float(raw_input())

# Verificar se deu a volta no ciclo.
if (angulo > angulo_total):
	angulo = angulo % angulo_total

# Verificando os quadrantes.
if (angulo > 0 and angulo < 90):
	print "Quadrante 1"
elif (angulo > 90 and angulo < 180):
	print "Quadrante 2"
elif (angulo > 180 and angulo < 270):
	print "Quadrante 3"
elif (angulo > 270 and angulo < 360):
	print "Quadrante 4"
elif (angulo == 0 or angulo == 90 or angulo == 180 or angulo == 270 or angulo == 360):
	print "Sobre eixos"

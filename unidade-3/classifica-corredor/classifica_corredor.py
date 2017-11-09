# coding: utf-8
# Aluno: Júlia Alves
# Matricula: 117211383
# Atividade: Classifica Corredor - Unidade 3

# Entrada dos dados de distância (km) e tempo (h)
distancia = float(raw_input())
tempo = float(raw_input())

# Calculando a velocidade média
velocidade = distancia / tempo

categoria = "profissional"

# Verifica a categoria que o corredor pertence.
if velocidade < 10.0:
    categoria = "amador"
elif 10.0 <= velocidade <= 15.0:
    categoria = "aspirante"

# Imprime a velocidade média e a categoria do corredor.
print "Velocidade: %.1fkm/h. Corredor %s." % (velocidade, categoria)

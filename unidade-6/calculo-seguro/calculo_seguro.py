# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Cálculo de Seguro - Unidade 6

# Verifica os pontos de acordo com a idade.	
def calcular_pontos_idade(idade):	
	if idade <= 21 or idade > 60:
		return 20
	elif 22 <= idade <= 30:
		return 15
	elif 31 <= idade <= 40: 
		return 12
		
	return 10

# Se Casado (True) retorna 10pts, se Solteiro retorna 20pts.
def verificar_casado(estado_civil):
	if estado_civil:
		return 10
	
	return 20

# Verifica área de risco do assegurado.
def verficar_area_risco(area_risco):
	if area_risco:
		return 20
	
	return 10

# Verifica se possui portão eletrônico.
def verificar_portao(portao_eletronico):
	if portao_eletronico:
		return 20
	
	return 10

# Verifica se reside em casa.
def verificar_moradia(moradia):
	if moradia:
		return 20
	
	return 10
	
# Verifica se reside em casa própria.
def verificar_casa_propria(casa_propria):
	if casa_propria:
		return 10
	
	return 20

# Verifica o tipo de uso do veículo.
def verificar_uso_veiculo(uso):
	if uso == "Lazer" or uso == "Misto":
		return 20
	
	return 10

# Calcula o valor do seguro.
def calcula_seguro(valor_veiculo, questionario):
	idade = questionario[0]
	estado_civil = questionario[1]
	area_risco = questionario[2]
	portao_eletronico = questionario[3]
	moradia = questionario[4]
	casa_propria = questionario[5]
	uso_veiculo = questionario[6]
	
	pontos = calcular_pontos_idade(idade)
	pontos += verificar_casado(estado_civil)
	pontos += verficar_area_risco(area_risco)
	pontos += verificar_portao(portao_eletronico)
	pontos += verificar_moradia(moradia)
	pontos += verificar_casa_propria(casa_propria)
	pontos += verificar_uso_veiculo(uso_veiculo)
	
	if pontos <= 80:
		valor_pago = 0.1 * valor_veiculo
		risco = "Risco Baixo"
	elif 80 < pontos <= 100:
		valor_pago = 0.2 * valor_veiculo
		risco = "Risco Medio"
	else:
		valor_pago = 0.3 * valor_veiculo
		risco = "Risco Alto"
		
	return [pontos, risco, valor_pago]

	



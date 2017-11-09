# coding: utf-8
# Aluno: Júlia Alves
# Matricula: 117211383
# Atividade: Depois do 13 - Unidade 3

# Definindo constante para número restritivo.
NUMERO_RESTRITO = 13

# Entrada dos números.
numero1 = int(raw_input())
numero2 = int(raw_input())
numero3 = int(raw_input())

resultado = numero1 + numero2 + numero3

# Verificando a ocorrência do número restrito.
if numero3 == NUMERO_RESTRITO:
    resultado = numero1 + numero2
elif numero2 == NUMERO_RESTRITO:
    resultado = numero1

if resultado == NUMERO_RESTRITO or numero1 == NUMERO_RESTRITO:
    resultado = 0

print resultado
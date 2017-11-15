# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Soma Últimos Ímpares - Unidade 4

# Entrada dos dados referente a quantidade de números e o número limite.
quantidade_numeros = int(raw_input())
numero_limite = int(raw_input())

impares = []

# Coleto todos os números ímpares informados pelo usuário.
for quantidade in range(quantidade_numeros):
    numero = int(raw_input())

    if numero % 2 != 0:
        impares.append(numero)

soma = 0
indices_inverso = range(-1, -(len(impares) + 1), -1)

# Faz o somatório dos números ímpares de forma inversa e verifica se não atinge o limite máximo.
for indice in indices_inverso:
    soma += impares[indice]

    if soma >= numero_limite:
        soma -= impares[indice]
        break

print soma
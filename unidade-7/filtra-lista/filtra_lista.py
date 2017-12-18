# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Filtra Lista - Unidade 7


# Retorna uma lista com os elementos onde a posição
# do elemento na lista original é divisível por divisor.
# Recebe como parâmetro o número inteiro (divisor) e uma
# lista não vazia de inteiros não-negativos.
def filtra_lista(divisor, numeros):
    divisiveis = []

    for indice in range(len(numeros)):
        if indice % divisor == 0:
            divisiveis.append(numeros[indice])

    return divisiveis

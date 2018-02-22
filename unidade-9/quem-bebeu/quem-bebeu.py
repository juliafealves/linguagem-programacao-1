# coding: utf-8
# Laboratório de Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Quem Bebeu Mais e Menos - Unidade 9


# Retorna a soma da coluna da matriz.
def soma_coluna(matriz, coluna):
    soma = 0

    for i in range(len(matriz)):
        soma += matriz[i][coluna]

    return soma


# Verifica qual amigo bebeu mais e menos de acordo com a matriz.
def quem_bebeu_mais_menos(sabado, domingo):
    quantidade_amigos = len(sabado)
    bebeu_mais = 1
    bebeu_menos = 1

    garrafas_sabado = soma_coluna(sabado, 0)
    garrafas_domingo = soma_coluna(domingo, 0)
    garrafas = garrafas_sabado + garrafas_domingo

    maior = garrafas
    menor = garrafas

    for i in range(1, quantidade_amigos):
        garrafas_sabado = soma_coluna(sabado, i)
        garrafas_domingo = soma_coluna(domingo, i)
        garrafas = garrafas_sabado + garrafas_domingo

        if garrafas > maior:
            if maior < menor:
                menor = maior
                bebeu_menos = bebeu_mais

            maior = garrafas
            bebeu_mais = i + 1
        else:
            if garrafas < menor:
                menor = garrafas
                bebeu_menos = i + 1

    return (bebeu_mais, bebeu_menos)

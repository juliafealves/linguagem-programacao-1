# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Valor Polinômio - Unidade 7


# Retorna o cálculo de um polinômio.
# Recebe como parâmetro um lista de coeficientes
# ordenado pelo índice. E valor a ser substituído no polinômio.
def valor_polinomio(polinomio, valor):
    resultado = 0

    for indice in range(len(polinomio)):
        resultado += (valor ** indice) * polinomio[indice]

    return resultado

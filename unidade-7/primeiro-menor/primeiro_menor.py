# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Primeiro Menor - Unidade 7


# Através do separador, "explode" os elementos
# e cria uma lista com os elementos.
def explode(cadeia, separador=" "):
    lista = []
    palavra = ""

    for caracter in cadeia:
        if caracter != separador:
            palavra += caracter
        else:
            lista.append(palavra)
            palavra = ""

    lista.append(palavra)

    return lista


# Retorna o índice do primeiro elemento menor
# que o parâmetro menor. Recebe um inteiro e uma lista de digitos (string)
def primeiro_menor(menor, numeros):
    for indice in range(len(numeros)):
        if int(numeros[indice]) < menor:
            return indice

    return -1


def main():
    # Recebe a string de números e o valor menor a ser localizado na lista
    numeros = raw_input()
    menor = int(raw_input())

    numeros = explode(numeros)

    # Busca o índice do primeiro menor.
    indice = primeiro_menor(menor, numeros)

    # Retorna o valor do primeiro menor.
    if indice != -1:
        print "primeiro menor que %i: %s" % (menor, numeros[indice])
    else:
        print "sem menores que %i" % menor


if __name__ == '__main__':
    main()

# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Peso Ideal com Função - Unidade 6

FEMININO = "F"
FIM_PROGRAMA = "****"


# Calcula o peso ideal de acordo com o sexo.
def calcular_peso(sexo, altura):
    if sexo.upper() == FEMININO:
        return 62.1 * altura - 44.7

    return 72.7 * altura - 58

sexos = []
pesos = []

# Recebe as entradas do programa.
while True:
    entrada = raw_input()

    if entrada == FIM_PROGRAMA:
        break

    entrada = entrada.split()
    sexo = entrada[0]
    altura = float(entrada[1])

    pesos.append(calcular_peso(sexo, altura))
    sexos.append(sexo)

# Imprime as saídas.
for indice in range(len(pesos)):
    sexo = "Homem"

    if sexos[indice].upper() == FEMININO:
        sexo = "Mulher"

    print "%s: peso ideal é %.1f" % (sexo, pesos[indice])

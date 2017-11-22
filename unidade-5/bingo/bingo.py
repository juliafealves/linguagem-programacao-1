# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Bingo - Unidade 5

# Recebe como entrada as duas cartelas dos jogadores.
cartela1 = raw_input()
cartela2 = raw_input()

# Como as cartelas só irão de 0 a 9 e não se repetem, então utiliza uma lista para "marcar"
# os números da cartela de cada jogador
jogador1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
jogador2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Utilizado para contabilizar o tamanho (quantidade de números) da cartela.
tamanho_cartela = 0

# "Marca" na lista os números das cartelas e soma o tamanho da cartela.
for indice in range(0, len(cartela1), 2):
    jogador1[int(cartela1[indice])] = 1
    jogador2[int(cartela2[indice])] = 1
    tamanho_cartela += 1


pontos_jogador1 = tamanho_cartela
pontos_jogador2 = tamanho_cartela

# Lê o número sorteado e caso exista na lista decrementa o pontos do jogador.
while pontos_jogador1 != 0 and pontos_jogador2 != 0:
    numero_sorteado = int(raw_input())

    if jogador1[numero_sorteado] == 1:
        pontos_jogador1 -= 1

    if jogador2[numero_sorteado] == 1:
        pontos_jogador2 -= 1

# Imprime o resultado do bingo.
if pontos_jogador1 == 0 and pontos_jogador2 == 0:
    print "Empate."
elif pontos_jogador1 == 0:
    print "Bingo! Jogador 1 venceu."
else:
    print "Bingo! Jogador 2 venceu."

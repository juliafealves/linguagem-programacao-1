# coding: utf-8
# Programação 1 - 2017.2 UFCG
# Aluna: Júlia Fernandes Alves (117211383)
# Atividade: Bingo - Unidade 5

cartela1 = raw_input()
cartela2 = raw_input()

jogador1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
jogador2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for indice in range(0, len(cartela1), 2):
    jogador1[int(cartela1[indice])] = 1
    jogador2[int(cartela2[indice])] = 1

sorteio = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print "j1", jogador1
print "j2", jogador2

while jogador1 != sorteio or jogador2 != sorteio:
    numero_sorteado = int(raw_input())
    jogador1[numero_sorteado] = 0
    jogador2[numero_sorteado] = 0

if jogador1 == sorteio and jogador2 == sorteio:
    print "Empate."
elif jogador1 == sorteio:
    print "Bingo! Jogador 1 venceu."
else:
    print "Bingo! Jogador 2 venceu."

# Pares de Múltiplos
Em determinada aplicação é necessário identificar em uma sequência, números vizinhos em que um é múltiplo do outro. Pede-se que você escreva um programa que lê uma sequência de valores e conta a quantidade de pares desse tipo.

**Exemplo.** Considere que se deseja encontrar quantos pares na sequência abaixo são o dobro um do outro.
```
3 7 4 8 12 6 4 5
```
O programa deverá identificar que a sequência contém 2 pares desse tipo: (4, 8) e (12, 6).

Já nesta outra sequência, há três pares em que um é o triplo do outro: (3, 9), (9, 27) e (2, 6).
```
5 2 3 9 27 7 2 6 4
```
## Entrada
O programa deve ler a sequência de números da primeira linha da entrada, separados por espaços. E da segunda linha da entrada, deve ler o fator que relaciona os dois números.

## Saída
O programa deve imprimir apenas o número de pares encontrados na sequência em que um dos valores é múltiplo de seu vizinho e, nas linhas seguintes, cada um desses pares.

###Exemplo de execução
Para o primeiro exemplo acima, a execução do programa seria:
```
$ python pares.py
3 7 4 8 12 6 4 5
2
2 par(es)
4 8
12 6
$ _
```
E para o segundo exemplo.
```
$ python pares.py
5 2 3 9 27 7 2 6 4
3
3 par(es)
3 9
9 27
2 6
$ _
```

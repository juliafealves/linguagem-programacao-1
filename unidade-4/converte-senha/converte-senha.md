# Criptografando uma Senha
É muito comum definir uma senha de uma conta a partir de uma palavra ou frase conhecida. Um truque bastante usado é usar
um esquema simples de criptografia que troca algumas letras da palavra escolhida para ser a base da senha. Escreva um 
programa que codifica palavras usando um sistema simples de criptografia que consiste na substituição das letras de uma
palavra por números considerando o seguinte mapeamento:

A letra a é substituída pelo número 4.
A letra e é substituída pelo número 3.
A letra i é substituída pelo número 1.
A letra o é substituída pelo número 0.

Importante considerar que a regra de conversão não se aplica na primeira letra da palavra.

## Entrada
O programa recebe da entrada uma palavra a ser convertida e imprime o resultado. Por simplificação, considere que as 
palavras recebidas da entrada são formadas apenas por letras e sem acentuação.

## Saída
O programa imprime na saída a palavra codificada e a quantidade de letras convertidas. Veja os exemplos de execução e 
observe a formatação definida.

Obs: Sua solução não deve conter funções prontas de Python que iterem sobre sequências.

###Exemplos de Execução
```
$ python codifica.py
Python
Pyth0n (1 troca(s))
$ python codifica.py
ZENIT
Z3N1T (2 troca(s))
$ python codifica.py
Abacateiro
Ab4c4t31r0 (5 troca(s))
```
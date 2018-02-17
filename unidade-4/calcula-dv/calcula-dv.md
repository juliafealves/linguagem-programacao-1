# Calcula DV
Escreva um programa que calcule o digito verificador de um número de conta de banco. Nesse banco o digito é calculado em
duas etapas. Primeiramente, a soma dos dígitos das posições pares é multiplicada pela soma dos dígitos das posições 
ímpares. O dígito verificador é obtido como sendo o resto da divisão do resultado da primeira etapa por 11. Se o resto 
da divisão for 10, contudo, deve ser substituído por 'X'. Assim, para o número 7130, por exemplo, o digito verificador 
é 'X' que é calculado por ((7 + 3) * (1 + 0)) % 11 = 10. Já para o número 7132, o digito verificador é '8', calculado 
por ((7 + 3) * (1 + 2)) % 11 = 8.

## Entrada
Seu programa deve ler um único número de banco da entrada.

## Saída
Seu programa deve imprimir o número com o respectivo digito verificador, separado com um hífen.

### Exemplos de execução
``` 
python solution.py
7130
7130-X

python solution.py
7132
7132-8
```
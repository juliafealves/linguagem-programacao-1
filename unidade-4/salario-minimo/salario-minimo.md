# Análise de Variação do Salário Mínimo
Um economista precisa analisar a variação do salário mínimo. Pede-se que você escreva um programa que dados os valores 
mensais do salário mínimo, determine quais deles ficaram acima de U$ 100.00 (cem dólares) e quais ficaram abaixo.

## Entrada
Da primeira linha da entrada, seu programa deve ler o ano inicial da série de dados. Da segunda linha da entrada, deve 
ler o ano final da série. Em seguida, deve ler os valores do salário mínimo em dólares para cada um dos anos da faixa 
indicada.

## Saída
Seu programa deve imprimir um relatório indicando em quantos anos o salário mínimo ficou acima de U$ 100.00 (cem 
dólares) e em quantos ficou abaixo (ou igual). Também deve indicar em que percentagem de anos da série o salário ficou 
nessas faixas de valores e a média dos salários naqueles anos. Se em nenhum ano da série o valor do salário mínimo 
estiver em uma das faixas, não é necessário imprimir a média de valores. Veja os exemplos de execução.

### Exemplo de Execução
```
$ python variacao_sm.py
1994
1996
68.93
109.41
112.90
1 ano(s) abaixo (33% dos anos)
média dos anos abaixo: U$ 68.93
2 ano(s) acima (67% dos anos)
média dos anos acima: U$ 111.16
$ python variacao_sm.py
1995
1996
109.41
112.90
0 ano(s) abaixo (0% dos anos)
2 ano(s) acima (100% dos anos)
média dos anos acima: U$ 111.16
```
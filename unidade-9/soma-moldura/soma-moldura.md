# Molduras em Matriz Quadrada
Matriz quadrada é um tipo especial de matriz que possui o mesmo número de linhas e o mesmo de colunas. Considere a 
matriz quadrada M abaixo de dimensão 4 (representada como lista de listas).

```
M = [[1,  2,  3,  4 ],
     [5,  6,  7,  8 ],
     [9,  10, 11, 12],
     [14, 15, 16, 17]]
```

Definimos `moldura_0` ou moldura nível 0 de uma matriz quadrada como sendo os elementos que compõem as bordas dessa matriz. 
No exemplo acima, a `moldura_0` seria formada pelos elementos 1, 2, 3, 4, 8, 12, 17, 16, 15, 14, 9 e 5. A `moldura_1` 
de M é formada pelos elementos que margeiam os elementos da moldura_0. Assim, nesse exemplo, a `moldura_1` seria formada
pelos seguintes elementos 6, 7, 11 e 10. Para ser considerado moldura, é necessário ter pelo menos 4 elementos.

Se considerarmos uma matriz quadrada genérica de dimensão `n`, em que `n >= 2`, é possível ter `n / 2` molduras. Por 
exemplo, para uma matriz quadrada de dimensão 6, poderíamos ter 3 níveis de moldura (`moldura_0`, `moldura_1` e 
`moldura_2`).

Escreva a função `soma_moldura(m, k)` que recebe uma matriz quadrada m e retorna a soma dos elementos da k-ésima moldura.

### Exemplo de Asserts
```
M = [[1,  2,  3,  4 ], [5,  6,  7,  8 ], [9,  10, 11, 12], [14, 15, 16, 17]]
assert soma_moldura(M, 0) == 106
assert soma_moldura(M, 1) == 34
```
# Busca Todos em Matriz
Escreva a função `busca_matriz(m, e)` que busca todas as ocorrências do elemento `e` na matriz `m` (representada na 
forma de lista de listas) e que retorna uma lista com os índices do elemento e ou uma lista vazia, caso o elemento não 
exista na matriz.

### Exemplos de asserts
```
matriz = [
    [2, 3, 5, 3, 1],
    [3, 2, 1, 5, 6],
    [1, 2, 3, 2, 1],
]
assert busca_matriz(matriz, 4) == []
assert set(busca_matriz(matriz, 3)) == set( [(0,1), (0,3), (1,0), (2,2)] )
```
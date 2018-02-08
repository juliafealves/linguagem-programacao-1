# Altera Vetor por Escalar

Escreva a função `altera_vetor_por_escalar(vetor, escalar)` que faça a multiplicação de vetor por um escalar. No lugar 
de retornar um novo vetor, a função deve alterar a lista vetor com o resultado desta multiplicação.

## Exemplos e Asserts

```
vetor_1 = [1, 2, 3]
assert altera_vetor_por_escalar(vetor_1, -1) == None
assert vetor_1 == [-1, -2, -3]
assert altera_vetor_por_escalar(vetor_1, 2) == None
assert vetor_1 == [-2, -4, -6]
```
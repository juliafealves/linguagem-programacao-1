# Quantos Comeram?

A famosa feijoada da cantina de Dona Inês acontece toda quinta-feira no DSC. Os alunos fazem seus pedidos em grupos e em fila. Ou seja, chega um grupo de alunos que pede 10 feijoadas, depois aparece outro grupo que pede 5 feijoadas e assim, por diante.

Dona Inês sempre prepara apenas feijoada suficiente para N pessoas. A demanda, contudo, é tipicamente maior ou igual ao que ela preparou. Quando a feijoada não é capaz de servir todos os alunos de um grupo, todos os alunos do grupo desistem de comer feijoada. Mesmo com feijoadas sobrando, Dona Inês também para de servir feijoadas depois que o primeiro grupo de alunos desistir de comer em sua cantina.

Pede-se que você escreva a função quantos_comeram(N, fila) que recebe a quantidade de feijoadas feitas por Do. Inês, e uma representação da fila de grupos de pedidos (cada valor na fila indica quantas feijoadas aquele grupo pediu), e que retorne quantas feijoadas foram, de fato, consumidas no dia.

Veja os asserts abaixo para entender melhor a semântica da função pedida.

```
assert quantos_comeram(10, [10, 10]) == 10
assert quantos_comeram(12, [10, 10]) == 10
assert quantos_comeram(2, [10, 10]) == 0
assert quantos_comeram(5, [2, 3, 5]) == 5
```

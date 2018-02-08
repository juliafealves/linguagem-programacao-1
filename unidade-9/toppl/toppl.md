# Toppl

O TOPPL é uma prova de proficiência em programação aplicada pela UFCG. Apenas estudantes que tenham se inscrito e que 
tenham média acima de certo valor mínimo podem fazer o TOPPL. Pede-se que você escreva a função `filtra_alunos()` que 
seleciona os alunos aptos a fazer a prova de acordo com essa condição.

O primeiro parâmetro recebido pela função é uma lista dos alunos da disciplina com suas respectivas médias, na forma de
uma lista de pares de matrículas e médias. O segundo é a lista das matrículas dos estudantes inscritos. O terceiro 
parâmetro é a média mínima necessária para estar apto a fazer o TOPPL.

Espera-se que a função tenha efeito colateral. Ela deve alterar o conteúdo da lista de alunos, eliminando dela todos 
os alunos que não estão aptos a fazer a prova, seja por não ter média suficiente, seja por não terem feito a inscrição.

A função deve ainda retornar o número de alunos que foram eliminados da lista. Veja os asserts para compreender melhor 
a semântica da função.

```
inscritos = [121, 123, 124]
alunos = [ (120,8.0), (121,7.5), (122,5.0), (123,6.0), (124,9.0), (125,4.0) ]
assert filtra_alunos(alunos, inscritos, 7.0) == 4
assert alunos == [ (121,7.5), (124,9.0) ]
```
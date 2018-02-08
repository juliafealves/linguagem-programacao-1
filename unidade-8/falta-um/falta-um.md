# Falta um
Teresa e Cristina são colecionadoras de rótulos de cerveja. Como são amigas, Teresa decidiu presentear Cristina com alguns rótulos. Assim, ela enviou pelo correio uma quantidade N de rótulos. Contudo, dessa vez, a empresa responsável pelo envio perdeu um dos rótulos enviados, uma vez que Cristina notou que havia apenas N-1.

Escreva a função encontra_rotulo_perdido(rotulos_enviados, rotulos_recebidos) que retorna o rótulo da lista de enviados que não aparece na lista de rótulos recebidos.

Você pode assumir que sempre haverá um rótulo que foi enviado por Teresa, mas não foi recebido por Cristina.

## Exemplos de asserts
```
l1 = ['skol', 'brahma', 'itaipava']
l2 = ['itaipava', 'brahma']
assert encontra_rotulo_perdido(l1,l2) == 'skol'
```
# Grep
Escreva um programa que leia uma palavra com 3 caracteres e verifique a ocorrência dessa palavra em frases também lidas
da entrada.

## Entrada
Seu programa deve ler da entrada padrão uma palavra de 3 caracteres, uma número N que determina quantas frases serão 
lidas e, em seguida, as N frases.

## Saída
Seu programa deve imprimir as frases em que a palavra chave de 3 caracteres aparece.

###Exemplo de execução
```
python grep.py
ola
3
um exemplo de frase
outro ola frase
outro ola frase
frase
```

Note que, assim que uma frase com a palavra chave é lida, ela é impressa novamente.

### Restrições
**Muito importante!** É proibido utilizar `in` para verificar se uma string está dentro de outra.
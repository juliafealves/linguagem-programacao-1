# Cria Senha

As senhas criadas por pessoas geralmente remetem a uma palavra ou frase familiar que é modificada de alguma forma a fim de torná-la difícil de decifrar. Os cadastros em formulários na Web costumam testar a segurança da senha caracterizando-a, por exemplo, como "forte" ou "fraca". Pede-se que você crie um programa para criar senhas.

### Entrada
Seu programa deve receber palavras e o nível de segurança ("forte" ou "fraco") desejado e deve gerar e imprimir as senhas geradas. O programa deve parar quando ler o marcador "*". Sua implementação deve conter a função criaSenhaFraca(palavra) que recebe a palavra informada pelo usuário e a utiliza para gerar a senha.

### Saída
A senha é formada pela palavra compreendida entre dois caracteres abre parêntesis e dois caracteres fecha parênteses. O programa deve conter, ainda, a função criaSenhaForte(palavra) que recebe a palavra informada pelo usuário, cria uma senha fraca (de acordo com a explicação anterior) e depois substitui caracteres de acordo com a seguinte política:

```
o,O -> 0
i,I,L,l -> 1
e,E -> 3
a,A -> 4
b,B -> 6
t,T -> 7
```

## Exemplo de execução do programa
```
$ python criasenha.py
alo fraco
antonio forte
***
((alo))
((4n70n10))
```
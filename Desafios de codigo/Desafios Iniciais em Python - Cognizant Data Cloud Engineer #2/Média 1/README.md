## Desafio

Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos portanto é 11). Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

## Entrada

O arquivo de entrada contém 2 valores com uma casa decimal cada um.

## Saída

Calcule e imprima a variável MEDIA conforme exemplo abaixo, com 5 dígitos após o ponto decimal e com um espaço em branco antes e depois da igualdade. Utilize variáveis de dupla precisão (double) e como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

| Exemplo de Entrada | Exemplo de Saída|
| ---|--- |
| 5.0<br />7.1 | MEDIA = 6.43182 |
| 0.0<br />7.1 | MEDIA = 4.84091 |
| 10.0<br />10.0 | MEDIA = 10.00000 |

	
```bash
a = float(input())
b = float(input())

#TODO: Complete os espaços em branco com as respectivas variáveis para o cálculo da média.
media = ( * 3.5 +  * 7.5) / 11

#TODO: Complete com a variável que representa o resultado da média.
print(f'MEDIA = { : .5f}')


```
	


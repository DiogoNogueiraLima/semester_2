# Questão 2

## Futuro do leão

### Tempo limite: 
75 ms

### Enunciado:
O jogador de futebol Luciano Juba está enfrentando uma decisão difícil. No fim do seu contrato com o pequeno clube de futebol Sport Recife, ele precisa decidir rapidamente se deve continuar jogando por um time que empata com um Santa Cruz que está na série D ou procura novos ares pelas outras regiões do Brasil, ou até mesmo na Europa.

Para tomar a melhor decisão possível para sua carreira, Juba precisa analisar qual salário será mais adequado para ser mencionado na mesa de negociações. Humilde como só ele, o cálculo a ser realizado por ser agente deve ser determinado pelas medianas dos salários do Sport e do seu futuro clube.

#### ATENÇÃO: Usar Mergesort!

### Input
O input é formado por dois arrays ordenados, o primeiro referente aos salários no Sport e o segundo aos salários no seu possível futuro clube. O formato das strings será uma lista simples de números inteiros separados por um espaço.

#### Exemplo:

1 2 2 3 4 5

5 5 8 11 15

### Output
'O salário sugerido por Juba na primeira negociação será de <-mediana> mil reais.'

Onde a mediana deve ser retornada com 2 casas decimais de precisão.

## Código de resolução:
```python
def merge(lista1, lista2, inicio=0, fim=None):
    if fim is None:
        fim = len(lista1) + len(lista2)
    left = lista1
    right = lista2
    top_left, top_right = 0, 0
    for k in range(inicio, fim+1):
        if fim//2 < k: # achando a mediana
            if (metade_tamanho_lista_final)%2 == 0:
                mediana = (float(lista_final[k-1])+float(lista_final[k-2]))/2
                print(f'O salário sugerido por Juba na primeira negociação será de {mediana}0 mil reais.')
                exit()
            else:
                print(f'O salário sugerido por Juba na primeira negociação será de {float(lista_final[k-1])}0 mil reais.')
                exit()


        elif int(top_left) >= len(left):
            lista_final[k] = right[top_right]
            top_right += 1
        elif int(top_right) >= len(right):
            lista_final[k] = left[top_left]
            top_left += 1
        elif int(left[top_left]) < int(right[top_right]):
            lista_final[k] = left[top_left]
            top_left += 1
        else:
            lista_final[k] = right[top_right]
            top_right += 1



# começando o codigo em si
salarios_sport = input().split()
salarios_vasco = input().split()

metade_tamanho_lista_final = (len(salarios_sport) + len(salarios_vasco))
lista_final = [None] * (metade_tamanho_lista_final//2 + 1)

# output
merge(salarios_sport, salarios_vasco)

'''Exemplos de Inputs:

17 25 42 150 159 213 395 456 456 486

22 104 121 204 224 248 286 457 469 495
'''

```

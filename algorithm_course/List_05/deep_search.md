# Questão 2

## MIM DÊ PAPAI

### Tempo limite: 
400 ms

### Enunciado:
Você é o gerente de marketing da Indústria Farinha na Cumbuca e precisa lançar um novo produto nas redes sociais, até que chegue no lobisomem pidão. Para isso, você precisa desenvolver uma estratégia eficiente de distribuição de informações, de forma a atingir o maior número possível de pessoas em um curto período de tempo.

Para elaborar essa estratégia, você precisa entender como funciona a dinâmica de compartilhamento de informações nas redes sociais. Em uma rede social com N usuários (vértices) e M conexões de amizade (arestas), o processo de distribuição de notícias funciona da seguinte maneira:

##### Um usuário i (1 <= i <= n) recebe a notícia de alguma fonte.

##### Esse usuário passa a notícia para seus amigos.

##### Os amigos repassam para seus amigos e assim em diante.

##### O processo acaba quando não há um par de amigos em que um sabe a notícia e o outro não.

Seu objetivo é determinar a quantidade de usuários que saberiam a notícia se cada usuário i (1 <= i <= n) iniciasse a distribuição. Para isso, você deve desenvolver um algoritmo que receba como entrada n, m e uma lista de conexões entre os usuários, e retorne uma lista com n inteiros, onde o i-ésimo inteiro representa o número de usuários que saberiam a notícia se o usuário i começar distribuindo-a. Utilize a busca em profundidade para verificar todos os nós adjacentes.

### Input
Na primeira linha você vai receber 2 valores N e M , onde N representa o número de usuários e M o número de conexões entre os usuários.

Seguido por X linhas com 2 inteiros U e V representando os usuários conectados.

### Output
Imprima N inteiros. O i-th inteiro deve ser igual ao número de usuários que saberiam a notícia se o usuário i começar distribuindo-a.

## Código de resolução:
```python
class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * vertices for i in range(vertices)]
        self.visitados = [False] * vertices

    def add_aresta(self, u, v):
        self.grafo[u - 1][v - 1] = 1
        self.grafo[v - 1][u - 1] = 1

    def dfs(self, u):
        global passos
        passos += 1
        self.visitados[u] = True
        for i in range(self.vertices):
            if self.grafo[u][i] == 1 and self.visitados[i] is False:
                self.dfs(i)
        

# recebendo a entrada
first_input = input().split()
tam_lista = int(first_input[0])
qnt_entradas = int(first_input[1])

# criando grafo
grafo = Grafo(tam_lista)

# loop para pegar as arestas e adicionar ao grafo
for i in range(qnt_entradas):
    input = input().split()   
    u = int(input[0])
    v = int(input[1])
    grafo.add_aresta(u, v)

    del input

# fazendo a busca partindo de cada elemento
for i in range(tam_lista):
    passos = 0
    grafo.dfs(i)
    if i == tam_lista - 1:
        print(passos)
    else:
        print(passos, end=' ')

    grafo.visitados = [False] * tam_lista

''' Exemplo de entrada:
7 5
1 7
4 1
3 6
4 6
2 5
'''
```

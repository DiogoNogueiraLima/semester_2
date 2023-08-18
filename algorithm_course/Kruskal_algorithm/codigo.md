# Tatamento da base de dados:

Primeiramente o código lê a base de dados que contém uma lista de valores numéricos com os vértices conectados e seus pesos, e dessa forma os transforma em um dataframe com três colunas, mostrando os vértices conectados e logo após o seu peso. Em seguida, é verificado o maior valor em cada uma das colunas "Vértice 1" e "Vértice 2", para determinar o número total de vértices, número de arestas também é calculado a partir do número de linhas no dataframe.

```python
import pandas as pd
import sys

with open('Base-de-Dados-Projeto-Algoritimo.txt') as f:
    data = f.read()
    
data_list = list(map(float, data.split()))

# Divide a lista em grupos de 3 elementos
data_list_3col = [(data_list[i], data_list[i+1], data_list[i+2]) for i in range(0, len(data_list), 3)]

# Cria o dataframe com 3 colunas
df = pd.DataFrame(data_list_3col, columns=["Vertice 1", "Vertice 2", "Peso"])

# Printando o data frame para vizualizaçao do usuário
print(df)

# Achando e printando a quantidade de verticies da base de dados

maior_valor_coluna_1 = df['Vertice 1'].max()
maior_valor_coluna_2 = df['Vertice 2'].max()

if maior_valor_coluna_1 >= maior_valor_coluna_2:
  qntd_v = int(maior_valor_coluna_1 + 1)
  print(f'O número de vertices é de: {qntd_v} ')
else:
  qntd_v = int(maior_valor_coluna_2 + 1)
  print(f'O número de vertices é de: {qntd_v} ')


# Printando a quantidade de arestas da base de dados

num_linhas = df.shape[0]
print(f"O número de arestas no dataframe é:{num_linhas}")
qntd_a = int(num_linhas)
```
![alt text](https://user-images.githubusercontent.com/115439066/261471297-78ed2486-c0f0-4a0b-b993-406a15164337.png)

# Criação e implementação do algoritmo

Após a exibiçao da base de dados, são implementadas duas funções no código para poder realizar o heap. Logo em seguida, é implementado o algoritmo de Kruskal para encontrar a árvore geradora mínima de um grafo usando um heap para armazenar as arestas. A cada interação, a aresta de menor peso é removida do heap e é adicionada à árvore geradora mínima, desde que não forme um ciclo. O algoritmo continua até que todas as arestas sejam adicionadas à árvore ou até que não haja mais arestas disponíveis para serem adicionadas.

```python
def heap_push(heap, item):
    heap.append(item)
    i = len(heap) - 1
    if i == 0:
        return
    parent = (i - 1) // 2
    while i > 0 and heap[parent][0] > heap[i][0]:
        heap[parent], heap[i] = heap[i], heap[parent]
        i = parent
        parent = (i - 1) // 2


def heap_pop(heap):
    if len(heap) == 0: # caso a nao tenha mais conexoes a fazer o codigo é finalizado
        print()
        print('Na base de dados nem todos os vertices são conectados, existem vertices que se conectam com apenas um ou dois vertices (como por exemplo os vertices 1800 com o 1801 e os 1900 com 1901 e 1902')
        print('Dito isso, seram formadas duas arvoreszinhas e uma arvore grandona e não apenas uma só arvore gigante com todos os nós')
        print(f'Aqui está em qual vertice principal está cada vertice fez conexão (onde o indice é qual o vertice olhado e o numero que aparece é o conjunto ao qual ele foi acoplado): {hash_n}')
        #print()
        #for i in list_conections:
            #print(i)# este aqui era para printar as ligaçoes dos vertices caso tivessem sido adicionados à lista de conexoes
        print()
        print(f'foram necessarias apenas {count} arestas com o custo total de {custo}')
        print()
        sys.exit()
        

    if len(heap) == 1:
        return heap.pop()

   
    top_item = heap[0]
    heap[0] = heap.pop()
    i = 0
    while True:
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        smallest = i

        if left_child < len(heap) and heap[left_child][0] < heap[smallest][0]:
            smallest = left_child

        if right_child < len(heap) and heap[right_child][0] < heap[smallest][0]:
            smallest = right_child

        if smallest == i:
            break

        heap[i], heap[smallest] = heap[smallest], heap[i]
        i = smallest

    return top_item

# criando o heap
heap = []

'''list_conections = []''' # lista de conexoes que ajudou na debugaçao do codigo para ver oq estava acontecendo

# criando um dicionario dos vericies caso os vertices nao estejam enumerados de 0 a qntd, mas como estão enumerados de 0 a qntd_v então nao será necessario
# dict = ['' for i in range(0, qntd_v)] # como nessa base de dados, os vertices ja estão enumerados em ordem crescente e constante de 0 a qnt_v, nao será necessario o uso desse dicionario


# recebendo quais sao as arestas e os pesos
'''n = 0'''
with open('Base-de-Dados-Projeto-Algoritimo.txt') as f:
    for i in range(qntd_a):
        linha = f.readline().strip()
        valores = linha.split(' ')
        if len(valores) == 3:
            v1, v2, peso = valores
            v1 = int(v1)
            v2 = int(v2)
            peso = float(peso)
        # fazendo o heap para colocar a aresta de menor peso na raiz
        heap_push(heap, (peso, v1, v2))

    # adicionando os vertices no dicionario caso fosse necessario
'''    if v1 not in dict:
        dict[n] = v1
        n += 1
    if v2 not in dict:
        dict[n] = v2
        n += 1
'''

# criando i conjuntos
conjuntos = [[''] for i in range(0, qntd_v)]

# colocando cada vertice no conjunto
for i in range(0, qntd_v):
    conjuntos[i][0] = i

# criando uma tabela para delegar para onde (local) vai cada nova aresta nos conjuntos
hash_n = [i for i in range(0, qntd_v)]  # hash[i] é o conjunto ao qual o vertice i pertence

# mostrando como ficaram os conjuntos e a tabela dos vertices, usado para o auxilio da debugação do codigo, mas nao necessario para o print
'''print(conjuntos)
print(hash_n)
'''
# contador de arestas lidas e o contador do custo da arvore geradora
count = 0
custo = 0

# loop até formar a arvore
print('A arvore geradora minima terá essas conexões:')
while count < (qntd_v - 1):
      peso, v1, v2 = heap_pop(heap)  # removendo a menor aresta do heap

      # pegando em qual conjunto o vertice olhado está
      first_v = hash_n[v1]  # caso estivesse usando o dicionario: first_v = hash_n[dict.index(v1)]
      second_v = hash_n[v2]  # caso estivesse usando o dicionario: second_v = hash_n[dict.index(v2)]

      # se a arvore que está o vertice A for diferente do vertice que tiver aresta B, juntamos as duas
      if first_v != second_v:

          # adicionando os vertices que fizeram a conexao e seu respectivo peso na lista de conexões, nao é necessario, mas é para deixar o codigo mais facil na hora de debugar
          '''dict_conection = [v1, v2, peso]
          list_conections.append(dict_conection)'''
          print(f'{v1} {v2} {peso}')

          custo += peso  # botando a aresta na arvore geradora
          if second_v < first_v:
              first_v, second_v = second_v, first_v  # trocando os valores dos vertices para ficar na ordem crescente
          for j in conjuntos[second_v]:
              hash_n[j] = first_v

          # fazendo a uniao dos conjuntos a e b
          conjuntos[first_v].extend(conjuntos[second_v])
          conjuntos[second_v] = []

          count += 1

    # mostrando como estao ficando os conjuntos e o hash dos vertices, util na hora da elaboraçao do codigo
'''    print(conjuntos)
    print(hash_n)'''

# mostrando quanto custaria caso fosse apenas uma árvore
print(custo)
```

# Conclusão

No final do código há uma verificação que faz a checagem e imprime uma mensagem de aviso caso alguns vértices não estejam conectados, indicando que o grafo é composto por mais de uma árvores. E após todo o processo, o código é finalizado printando como é feita a árvore geradora mínima (quais nós estão ligados e seu respectivo peso) e, por fim, o seu custo total da árvore (o peso de todas as arestas da(s) árvore(s) gerada(s)).

![alt text](https://user-images.githubusercontent.com/115439066/261473633-761b43b8-b152-4246-8d8a-03117836287c.png)

![alt text](https://user-images.githubusercontent.com/115439066/261471994-b0dc259c-89d3-4082-89c4-f21217c06725.png)

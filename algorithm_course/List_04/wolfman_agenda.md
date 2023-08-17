# Questão 3

## Wolfman Agenda

### Tempo limite: 
750 ms

### Enunciado:
Ao viajar no verão para a casa do seu bom e velho tio Guillhermo Totoro, ele te ensina um antigo jogo desenvolvido nos tempos medievais para crianças passarem o tempo e evitarem caminhar por florestas escuras em busca de aventuras insalubres.

No início da partida, o jogador recebe uma sequência de inteiros e uma constante. A cada rodada, algumas operações devem ser realizadas:

##### Remover o maior valor da sequência

##### K = maximo - | minimo * constante |

###### Se K for maior que zero, insere K na sequência

O jogo deve acabar quando todos os números da sequência forem removidos.

#### ATENÇÃO: Usar Heap! Obviamente, é proibido usar comandos como max(), min() e sort().

### Input
Serão dadas duas linhas de entrada, referentes à sequência de números e à constante.

#### Exemplo:

5 5 8 11

2

### Output
O retorno do programa deve ser a quantidade de rodadas necessárias para que a partida acabe.

#### Exemplo:

12 rodadas, partindo para a próxima!

## Código de resolução:
```python
# heap de maximo
def heapsort_max(arr):
    n = len(arr)
    
    # Construir uma heap máxima
    for i in range(n // 2 - 1, -1, -1):
        heapify_max(arr, n, i)

    arr[0], arr[len(lista_inteiros)-1] = arr[len(lista_inteiros)-1], arr[0]

def heapify_max(arr, n, i):
    # Encontrar o maior elemento entre a raiz e seus filhos
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and int(arr[left]) > int(arr[largest]):
        largest = left
    
    if right < n and int(arr[right]) > int(arr[largest]):
        largest = right
    
    # Trocar a raiz com o maior elemento
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        
        # Reestruturar a sub-heap afetada
        heapify_max(arr, n, largest)
        
# heap de minimo        
def heapify(arr, n, i):
    smallest = i
    left = 2 * i +1
    right = 2 * i + 2

    if left < n and int(arr[left]) < int(arr[smallest]):
        smallest = left

    if right < n and int(arr[right]) < int(arr[smallest]):
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)
        
def heapsort_min(arr):
    n = len(arr)
    
    # construir uma heap mínima
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


# recebendo as entradas e transformado-as em inteiros
lista_inteiros = input().split()
'''lista_inteiros[:] = list(map(int, lista_inteiros))'''
constante = int(input())

# criando um loop até que acabe as rodadas
rodada = 0
min_value = [None]
heapsort_min(lista_inteiros)
min_value[0] = lista_inteiros[0]
while lista_inteiros: # armazenar em algum lugar o minimo para nao precisar fazer dnv
    heapsort_max(lista_inteiros)
    k = int(lista_inteiros[len(lista_inteiros) - 1]) - (abs((int(min_value[0])) * constante))

    if k > 0:
        lista_inteiros[len(lista_inteiros) - 1] = k
        if k < int(min_value[0]):
            min_value[0] = k
    else:
        lista_inteiros.pop()
    rodada += 1
print(f'{rodada} rodadas, partindo para a próxima!')

''' Exemplos de Inputs:

5 5 8 11 
2

8 3 4 4 5 5 1 7
2
'''
```

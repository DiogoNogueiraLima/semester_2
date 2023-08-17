# Questão 1

## Paciência infinita

### Tempo limite: 
3000 ms

### Enunciado:
Chegada a segunda-feira, cinco estagiários da biblioteca imaginária do CIn foram encarregados de ordenar os novos livros disponibilizados pela reitoria do campus para decorar as prateleiras da instituição com infinito conhecimento.

Sendo cada um deles uma entidade incorpórea, uma inteligência artificial, um figmento de insônia, eles resolvem criar uma competição que analisa qual o método mais eficiente para ordenar cada pilha, através de algoritmos diferentes que foram estudados na matéria IF969.

    O primeiro estagiário, Caça-Rato, irá executar o método Bubble Sort.

    O segundo estagiário, Grafite, irá executar o método Selection Sort.

    O terceiro estagiário, Lacraia, irá executar o método Insertion Sort.

    O quarto estagiário, Rivaldo, irá executar o método Shell Sort.

    O quinto estagiário, Toninho, irá executar o método Quicksort (Hoare partition).

Para cada rodada da competição, os estagiários devem ordenar a mesma pilha de livros com o método delegado a eles, contando a quantidade de vezes que eles fazem uma comparação entre dois livros e a quantidade de vezes que eles trocam a posição de dois livros. Ao final da rodada, é definido o vencedor da rodada de acordo com a quantidade total de ações realizadas (comparações + trocas) para ordenar a pilha.

Após isso, os estagiários mais lentos tentam novamente ordenar a pilha, mas executando apenas a quantidade de ações que foram necessárias para o vencedor concluir a tarefa. Toninho, no entanto, não estava muito disposto a participar dessa etapa, então decidiu ficar de fora.
### Input
O código terá apenas uma linha de input, uma string de números únicos (sem repetições) separados por um espaço.

Exemplo: 4 5 8 7 14 2 3 6 21 32 52 0 2156 23

### Output
Na primeira etapa, deve ser retornado o resultado da ordenação da seguinte maneira para cada um dos estagiários:

<-nomeEstagiário> ordena a lista com <númeroComp> comparações e <númeroTrocas> trocas.

Após os cinco estagiários realizarem suas tarefas, devem ser retornado o nome do vencedor:

"-VENCEDOR DA RODADA-"

O vencedor da rodada é <-nomeEstagiário>, com <-númeroAções> ações.

Para a segunda etapa, lembre-se que Toninho não irá participar, então:

Os outros estagiários retornam as seguintes listas com essa quantidade de ações:

-Toninho está a dormir...-

Com <-númeroAções> ações <nomeEstagiário> ordena a lista assim: <-listaInterrompida> para cada um dos outros 4 estagiários (menos o vencedor, caso ele esteja entre os quatro).

## Código de resolução:
```python
def bubblesortcount(lista):
    global ondernaçao_bubble
    global troca_bubble
    arr = lista.copy()
    n = len(arr)
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                troca_bubble += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

            ondernaçao_bubble += 1

def bubble_sort(lista, interacoes):
    arr = lista.copy()
    n = len(arr)
    n = len(arr)
    count = 0
    # Loop externo para percorrer todos os elementos
    for i in range(n):
        # Loop interno para comparar elementos adjacentes
        for j in range(0, n-i-1):
            # Se o elemento atual for maior que o próximo
            if arr[j] > arr[j+1]:
                count += 1
                if count == interacoes:
                    return arr
                # Troca os elementos
                arr[j], arr[j+1] = arr[j+1], arr[j]   
            count += 1
            if count == interacoes:
                return arr


def selectionsortcount(arr):
    global ondernaçao_selection
    global troca_selection
    lista = arr.copy()
    tamanho = len(lista)
    for i in range(tamanho):
        menor = i
        for j in range(i + 1, tamanho):
            if lista[j] < lista[menor]:
                menor = j
            ondernaçao_selection += 1
        if i != menor:
            lista[i], lista[menor] = lista[menor], lista[i]
            troca_selection += 1
        if troca_selection == tamanho - 1:
            break
    
def selectionsort(arr, interacoes):
    lista = arr.copy()
    tamanho = len(lista)
    count = 0
    for i in range(tamanho):
        menor = i
        for j in range(i + 1, tamanho):
            if lista[j] < lista[menor]:
                menor = j
            count += 1
            if count == interacoes:
                return lista
            
        if i != menor:
            lista[i], lista[menor] = lista[menor], lista[i]
            count += 1
            if count == interacoes:
                return lista


def inserctionsortcount(arr):
    global ondernaçao_insertion
    global troca_insertion
    lista = arr.copy()
    tamanho = len(lista)

    for i in range(1, tamanho):
        chave = lista[i]
        j = i - 1
        while j >= 0 and chave < lista[j]:
            ondernaçao_insertion += 1
            lista[j + 1] = lista[j]
            j -= 1
            troca_insertion += 1
        
        if j != i-1:
            lista[j + 1] = chave
          
        if j >= 0:
            ondernaçao_insertion += 1
        

def inserctionsort(arr, interacoes):
    count = 0
    lista = arr.copy()
    tamanho = len(lista)

    for i in range(1, tamanho):
        chave = lista[i]
        j = i - 1
        while j >= 0 and chave < lista[j]:
            count += 1
            if count == interacoes:
              return lista
            lista[j + 1] = lista[j]
            j -= 1
            count += 1
            if count == interacoes:
              return lista
        
        if j != i-1:
            lista[j + 1] = chave
          
        if j >= 0:
            count += 1
            if count == interacoes:
              return lista
            
            
def shellsortcount(arr):
    global ondernaçao_shell
    global troca_shell
    lista = arr.copy()
    tamanho = len(lista)
    lacuna = tamanho // 2
    
    while lacuna > 0:
        for i in range(lacuna, tamanho):
            valor = lista[i]
            j = i
            while j >= lacuna and lista[j - lacuna] > valor:
                ondernaçao_shell += 1
                lista[j] = lista[j - lacuna]
                j -= lacuna
                troca_shell += 1
            lista[j] = valor
            
            ondernaçao_shell += 1 if j>= lacuna else 0
        lacuna //= 2
          


def shellsort(arr, interacoes):
    lista = arr.copy()
    tamanho = len(lista)
    lacuna = tamanho // 2
    count = 0
    
    while lacuna > 0:
        for i in range(lacuna, tamanho):
            valor = lista[i]
            j = i
            while j >= lacuna and lista[j - lacuna] > valor:
                count += 1
                if count == interacoes:
                  return lista
                lista[j] = lista[j - lacuna]
                j -= lacuna
                count += 1
                if count == interacoes:
                    return lista
            lista[j] = valor
            count += 1 if j>= lacuna else 0
            if count == interacoes:
                  return lista
            
        lacuna //= 2



def quicksort(A, lo, hi):
  global ondernaçao_quick
  global troca_quick
  if lo >= 0 and hi >= 0 and lo < hi:
    p = partition(A, lo, hi)
    quicksort(A, lo, p)
    quicksort(A, p + 1, hi)

def partition(A, lo, hi):
  global ondernaçao_quick
  global troca_quick
  pivot = A[(hi + lo) // 2]
  i = lo
  j = hi
  while True:
    if i >= j:
      return j
    while A[i] < pivot:
      ondernaçao_quick += 1
      i += 1
    while A[j] > pivot:
      ondernaçao_quick += 1
      j -= 1
    troca_quick += 1
    A[i], A[j] = A[j], A[i]


# quantidades de interaçoes de cada algoritmo
ondernaçao_bubble = 0
troca_bubble = 0
ondernaçao_selection = 0
troca_selection = 0
ondernaçao_insertion = 0
troca_insertion = 0
ondernaçao_shell = 0
troca_shell = 0
ondernaçao_quick = 0
troca_quick = 0

# começando em si o codigo
lista_inteiros = input().split()
lista_inteiros[:] = list(map(int, lista_inteiros))
arr = lista_inteiros.copy()

bubblesortcount(lista_inteiros)
final_bubble = ondernaçao_bubble + troca_bubble

selectionsortcount(lista_inteiros)
final_selection = ondernaçao_selection + troca_selection

inserctionsortcount(lista_inteiros)
final_insertion = ondernaçao_insertion + troca_insertion

shellsortcount(lista_inteiros)
final_shell = ondernaçao_shell + troca_shell

quicksort(arr, 0, (len(lista_inteiros)-1))
final_quick = ondernaçao_quick + troca_quick 

# print
primeira_interaçao_lista = [final_bubble, 'Caça-Rato']

if final_selection < final_bubble:
    primeira_interaçao_lista[0] = final_selection
    primeira_interaçao_lista[1] = 'Grafite'

if final_insertion < primeira_interaçao_lista[0]:
    primeira_interaçao_lista[0] = final_insertion
    primeira_interaçao_lista[1] = 'Lacraia'

if final_shell < primeira_interaçao_lista[0]:
    primeira_interaçao_lista[0] = final_shell
    primeira_interaçao_lista[1] = 'Rivaldo'

if final_quick < primeira_interaçao_lista[0]:
    primeira_interaçao_lista[0] = final_quick
    primeira_interaçao_lista[1] = 'Toninho'
interacoes = primeira_interaçao_lista[0]

# seçao prints
print(f'Caça-Rato ordena a lista com {ondernaçao_bubble} comparações e {troca_bubble} trocas.')
print(f'Grafite ordena a lista com {ondernaçao_selection} comparações e {troca_selection} trocas.')
print(f'Lacraia ordena a lista com {ondernaçao_insertion} comparações e {troca_insertion} trocas.')
print(f'Rivaldo ordena a lista com {ondernaçao_shell} comparações e {troca_shell} trocas.')
print(f'Toninho ordena a lista com {ondernaçao_quick} comparações e {troca_quick} trocas.')

print("-VENCEDOR DA RODADA-")
print(f'O vencedor da rodada é {primeira_interaçao_lista[1]}, com {interacoes} ações.')

print('-Toninho está a dormir...-')

print('Os outros estagiários retornam as seguintes listas com essa quantidade de ações:')
if primeira_interaçao_lista[1] == 'Caça-Rato':
    print(f'Com {interacoes} ações, Grafite ordena a lista assim: {selectionsort(lista_inteiros, interacoes)}')
    print(f'Com {interacoes} ações, Lacraia ordena a lista assim: {inserctionsort(lista_inteiros, interacoes)}')
    print(f'Com {interacoes} ações, Rivaldo ordena a lista assim: {shellsort(lista_inteiros, interacoes)}')

elif primeira_interaçao_lista[1] == 'Grafite':
    print(f'Com {interacoes} ações, Caça-Rato ordena a lista assim: {bubble_sort(lista_inteiros, interacoes)}')
    print(f'Com {interacoes} ações, Lacraia ordena a lista assim: {inserctionsort(lista_inteiros, interacoes)}')
    print(f'Com {interacoes} ações, Rivaldo ordena a lista assim: {shellsort(lista_inteiros, interacoes)}')
    
elif primeira_interaçao_lista[1] == 'Lacraia':
    print(f'Com {interacoes} ações, Caça-Rato ordena a lista assim: {bubble_sort(lista_inteiros, interacoes)}')
    print(f'Com {interacoes} ações, Grafite ordena a lista assim: {selectionsort(lista_inteiros, interacoes)}')
    print(f'Com {interacoes} ações, Rivaldo ordena a lista assim: {shellsort(lista_inteiros, interacoes)}')

elif primeira_interaçao_lista[1] == 'Rivaldo':
    print(f'Com {interacoes} ações, Caça-Rato ordena a lista assim: {bubble_sort(lista_inteiros, interacoes)}')
    print(f'Com {interacoes} ações, Grafite ordena a lista assim: {selectionsort(lista_inteiros, interacoes)}')
    print(f'Com {interacoes} ações, Lacraia ordena a lista assim: {inserctionsort(lista_inteiros, interacoes)}')

else:
    print(f'Com {interacoes} ações, Caça-Rato ordena a lista assim: {bubble_sort(lista_inteiros, interacoes)}')
    print(f'Com {interacoes} ações, Grafite ordena a lista assim: {selectionsort(lista_inteiros, interacoes)}')
    print(f'Com {interacoes} ações, Lacraia ordena a lista assim: {inserctionsort(lista_inteiros, interacoes)}')
    print(f'Com {interacoes} ações, Rivaldo ordena a lista assim: {shellsort(lista_inteiros, interacoes)}')

''' Exemplos de entradas:
863 399 632 305 599 943 244 859 893 564

9 8 7 6 5 4 3 2 1 0
'''
```

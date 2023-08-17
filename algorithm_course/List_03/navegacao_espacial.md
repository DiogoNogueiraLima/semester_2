# Questão 2

## Navegação Espacial

### Tempo limite: 
200 ms

### Enunciado:
Imagine que você é um cientista espacial encarregado de organizar o armazenamento de dados em uma nave espacial gigantesca. Sua missão é garantir que as informações sejam acessadas rapidamente em caso de emergência. Para isso, você decide aplicar seus conhecimentos em algoritmos e estruturas de dados para organizar o centro de dados da nave.

A quantidade de espaço disponível na nave irá variar de acordo com o tipo de nave, mas uma coisa é certa - cada espaço pode armazenar apenas um conjunto de dados. Você receberá códigos que representam os dados e terá que distribuí-los de acordo com a seguinte lógica:

    X mod N

Onde X é o código do dado e N é o número de espaços disponíveis no centro de dados da nave. Se um espaço já estiver ocupado, você precisará desenvolver um programa que possa encontrar um novo espaço para armazenar os dados.

Sua missão é garantir que os dados na nave espacial estejam armazenados e gerenciados de forma eficiente, para que a nave possa atender suas necessidades de missão com rapidez e precisão.

#### COMANDOS:

    ADD X -> Adiciona o código do dado X ao seu espaço de memoria correspondente.

    SCH D -> Eventualmente você poderá consultar se um dado foi adicionado a memória, para isso você receberá o dado D para consulta.

    CAP M -> Você poderá fazer consultas sobre o armazenamento daquele endereço de memória, para isso você receberá M representando o número de memória que precisará informar sua disponibilidade armazenamento.

### Input
Inicialmente teremos um valor N, o N informará a quantidade de espaços de memoria que o data center tem.

N       

Logo em seguida, será dado um C informando quantos comandos serão executados.

C

Após isso, seguem C linhas com as operações "ADD X", "CAP M" ou "SEARCH D".

Comando 1

Comando 2

...

Comando C

### Output
Quando o dado é adicionado, você deverá imprimir o número da posição da memória no data center: " E: E".

Quando quiser saber consultar se um dado já se encontra armazenado (comando SCH) você devera imprimir "NE" (Quando não for encontrado) ou "E: E" (O endereço que foi encontrado).

Quando quiser saber consultar um espaço de memoria (comando CAP) você deverá imprimir, "D"(Se estiver disponível para armazenar) ou "A: D" (O dado no endereço).

Quando o Data center não tiver mais nenhum endereço de memória disponível, você deverá imprimir "Toda memoria utilizada" e será finalizado o programa.

## Código de resolução:
```python
class HashTable:
    def __init__(self, table_size): # passa o tamanho da lista que quer criar
        if table_size < 1:
            raise IndexError('tamanho da lista tem que ser POSITIVO')
        
        else:
            self._size = 0
            self.table_size = table_size
            self.table = [[] for i in range(table_size)] # criando uma lista de espaços para armazenar os valores

    def hash_func(self, key): # retorna ONDE (em qual SLOT) o elemento dado irá entrar
        return key % self.table_size
    
    def __len__(self): # retorna o TAMANHO da lista
        return self._size
    
    def insert(self, key): # insere o elemento NO SLOT correto (slot descoberto com a funçao hash)
        if self.table[self.hash_func(key)] == []: # se o slot estiver vazio add o elemento nele
            self.table[self.hash_func(key)].append(key)
            self._size += 1
            insert_list.append(self.hash_func(key))

        else: # se o slot estiver cheio add no proximo slot
            self.insert(key+1)
        return

    def search(self, key, local): # insere o elemento NO SLOT correto (slot descoberto com a funçao hash)
        which_list = self.hash_func(local)
        if self.table[which_list]:
            if key in self.table[which_list]:
                return which_list # se a o elemento estiver na lista
            else:
                if self.table[which_list] and len(comparator_list) < (self.table_size):
                    comparator_list.append(0) # para impedir que a funçao entre em loop eterno se a lista estiver cheia
                    self.search(key, key+len(comparator_list))
                
        return False # se o elemento nao estiver na lista
        
    def consulta(self, memory_space): # insere o elemento NO SLOT correto (slot descoberto com a funçao hash)
        if self.table[memory_space]:
            return self.table[memory_space] # se a o elemento estiver na lista
        else:
            return False # se o elemento nao estiver na lista
        

# começando em si
table_size = int(input())
qnt_comandos = int(input())
hash = HashTable(table_size)

for i in range(qnt_comandos):
    insert_list = []
    comparator_list = []
    # ajeitando os valores a cada loop e recebendo a nova entrada
    entrada = input().split()
    comando = entrada[0]
    elem = int(entrada[1])

    if comando == 'ADD':
        hash.insert(elem)
        print(f'E: {insert_list[0]}')

    elif comando == 'SCH':
        encontrado = hash.search(elem, elem)
        if encontrado is False: # caso nao encontre o numero
            print('NE')
        else:  # funçao que vai procurar o numero na lista de numeros, se encontrar printa o num
            print(f'E: {encontrado}')


    elif comando == 'CAP':
        if int(table_size) == len(hash):
            print('Toda memoria utilizada')

        else:
            espaço = hash.consulta(elem)
            if espaço is False:
                print('D')
            else:
                print(f'A: {espaço[0]}')

    else:
        print('SÓ JESUS NA CAUSA')

    del entrada

''' Exemplo de entrada:
10
15
ADD 25
ADD 79
ADD 62
CAP 9
ADD 70
ADD 41
CAP 2
ADD 86
CAP 3
CAP 0
CAP 5
SCH 41
SCH 70
CAP 1
SCH 9


18
25
ADD 253775
ADD 620171
ADD 621658
CAP 12
ADD 754898
ADD 417017
CAP 2
ADD 864301
CAP 3
'''
```

# Questão 2

## CIn Core

### Tempo limite: 
350 ms

### Enunciado:
Os processadores modernos utilizam vários níveis de cache para acelerar o acesso à memória RAM. Esses caches armazenam as informações mais utilizadas pelo processador, favorecendo consultas a posições de memória que se repetem durante a execução de um processo. Isso diminui a latência média entre o processador e a memória RAM, melhorando significativamente o desempenho geral do sistema.

O processador CIn Core é um exemplo de processador que possui essa característica e utiliza uma estrutura de dados reativa a consultas repetitivas, ou seja, quanto mais um dado é requisitado, mais fácil é obtê-lo, pois ele estará armazenado em um dos níveis de cache do processador. Isso reduz ainda mais a latência e melhora a velocidade de processamento. Como entusiasta de processadores, você deseja explicar essa tecnologia para seus amigos Matheus, Isabelle e Arthur, para que eles entendam como ela pode melhorar o desempenho de seus sistemas.

Para conseguir explicar aos seus amigos, você chega a conclusão que o melhor a ser feito é utilizar uma estrutura de árvore, onde a cada consulta na estrutura além da entrega de dados o dado consultado deve ir para o topo. No trecho abaixo, pode-se observar o nó de valor 5 subindo na árvore.

#### Observações:

    1: A entrada não terá elementos repetidos.

    2: A estrutura a ser utilizada é a árvore de busca binária.

    3: Não é permitido o uso de bibliotecas.

### Input
Várias linhas com as seguintes operações:

    ADD V - Adiciona um valor V na estrutura.

    SCH V - Procura pelo valor V na estrutura.

### Output
Para a operação de ADD:

    CL(current level) - Onde CL representa o nível em que o dado V foi inserido.

Para a operação de SCH:

    PL(previous level) - Onde PL representa em que nível o dado V estava antes de ir para o topo ou -1 caso o valor não exista na estrutura.

## Código de resolução:
```python
ROOT = 'root'
class TreeNode: # criando a classe dos nos da arvore
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.dad = None
        self.height = 1

    def __str__(self):
        return str(self.data)
        
# Árvore Binária de Busca
class BinarySearchTree:
    def __init__(self):
        self._size = 0
        self.root = None

    def height(self, node): # define a altura partindo de um no especifico da arvore, importante para a funçao do balance
        if node:
            return node.height
        else:
            return 0
    
    def final_height(self, node=None): # a altura da arvore
        if node is None:
            node = self.root

        hleft = 0
        hright = 0

        if node.left:
            hleft = self.final_height(node.left)
        if node.right:
            hright = self.final_height(node.right)
        if hright > hleft:
            return hright + 1
        return hleft + 1

    def insert(self, data, count=0):  # adicionando um novo elemento
        if self.root is not None:
            self.root = self._insert(data, self.root, count)

        else: # se for o primeiro elemento a ser adicionado
            self.root = TreeNode(data)

    def _insert(self, value, node=None, count=0):
        if node is None:
            return TreeNode(value)
        
        elif int(value) < int(node.data): # se o valor adiconado for MENOR que o valor do no olhado
            node.left = self._insert(value, node.left, 1)
            node.left.dad = node
            lista_append.append(0) # adiciona um elemento qlqr na lista so para a fazer a contagem de qnts vezes foi chamada a funçao
        else:                # se o valor adivionado for MAIOR que o valor do no olhado
            node.right = self._insert(value, node.right, 1)
            node.right.dad = node
            lista_append.append(0) # adiciona um elemento qlqr na lista so para a fazer a contagem de qnts nós pai visitou

        # atualizand o tamanho e a altura
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        
        return node

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, node): # retorna a altura que o nó procurado se encontra

        if node is None:
            print(-1)
            return node
        
        if value == node.data:

            if value == self.root.data: # se o valor olhado for a RAIZ
                print(0)
                return node

            else:
                altura = (int(self.final_height()) - int(self.height(node))) # ta dando erro no self.height, a altura nao está vindo certa
                print(altura)
                fim = False
                while fim == False:
                    if altura == 0: # PARAR quando o nó chegar à RAIZ
                        fim = True
                    elif int(node.data) < int(node.dad.data): # se o nó pai for MAIOR que o no observado, rotaciona a subarvore p DIREITA
                        self.rotacionar_direita(node.dad)

                    elif int(node.dad.data) < int(node.data): # se o nó pai for MENOR que o no observado, rotaciona a subarvore p ESQUERDA
                        self.rotacionar_esquerda(node.dad)
                    altura -= 1

                return node
        
        elif int(value) < int(node.data):
            return self._search(value, node.left)
        return self._search(value, node.right)

    def rotacionar_esquerda(self, node):
        right = node.right
        node.right = right.left
        if right.left != None:
            right.left.dad = node

        right.dad = node.dad
        if node.dad == None:
            self.root = right
        elif node == node.dad.left:
            node.dad.left = right
        else:
            node.dad.right = right
        right.left = node
        node.dad = right

        # atualizando a altura
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def rotacionar_direita(self, node):
        left = node.left
        node.left = left.right
        if left.right != None:
            left.right.dad = node

        left.dad = node.dad
        if node.dad == None:
            self.root = left
        elif node == node.dad.right:
            node.dad.right = left
        else:
            node.dad.left = left

        left.right = node
        node.dad = left

        # atualizando a altura
        node.height = 1 + max(self.height(node.left), self.height(node.right))




# COMEÇANDO O CODIGO EM SI
lista_append = []
arvore = BinarySearchTree()
receber = True
while receber == True:

    try:
        input = input().split()
        if input[0] == 'ADD':
            arvore.insert(input[1])
            print(len(lista_append))


        elif input[0] == 'SCH':
            arvore.search(input[1])

        else:
            print('BOA NOITE AMIGOS E AMIGAS')
            print('ESTEVAO FERREIRA')


    except: # caso nao receba nenhuma entrada, o programa irá finalizar
        receber = False
        exit()

    lista_append = [] # resentando a lista da altura do nó
    del input

''' Exemplos de entradas:
ADD 165544
ADD 11623
SCH 165544
SCH 165544
SCH 11623

ADD 100
ADD 50
ADD 25
ADD 10
SCH 10
SCH 55
SCH 50
SCH 50

ADD 2959326
ADD 2890905
ADD 5123583
ADD 2595233
ADD 3841298
ADD 928157
ADD 5412099
ADD 8863313
ADD 8573267
ADD 6366716
ADD 365196
ADD 1888889
ADD 9306664
ADD 5656737
ADD 276724
ADD 5298987
ADD 6422248
ADD 820968
ADD 7958886
ADD 6186974

0
1
1
2
2
3
2
3
4
5
4
4
4
6
5
3
6
5
7
7

'''
```

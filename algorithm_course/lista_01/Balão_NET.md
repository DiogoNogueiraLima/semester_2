# Questão 3

## Balão NET

### Tempo limite: 
400 ms

### Enunciado:
Você foi contratado pela Balão NET para desenvolver um sistema de histórico de pesquisas em seu mais novo navegador, o "balão_explorer”. Para isso foi requisitada a utilização de uma lista duplamente encadeada para armazenar as pesquisas e também 4 funcionalidades básicas do sistema: busca, remoção, adição e exibição do histórico.

### Input
O programa receberá uma quantidade indefinida de entradas e deverá encerrar quando o comando final “END” for dado . Comandos :

    ADD X (X poderá ser qualquer string)

    REM X (X poderá ser qualquer string)

    EXIB

    FIND X (X poderá ser qualquer string , desde que contida na lista)

    END

o comando ADD deverá inserir o elemento na sua lista duplamente encadeada

o comando REM deverá remover o elemento na sua lista duplamente encadeada

o comando EXIB deverá printar todo o histórico contido na lista

o comando FIND deverá localizar um elemento já existente na lista e colocá-lo na primeira posição dela

### exemplo :

    lista = d - b - c - a

    FIND(“a”)

    EXIB

    resultado da lista = a - d - b - c

### Output
Após o comando EXIB será imprimido o histórico, exemplo:

site1.com.br

site2.com.br

...

## Código de resolução:
```python
class Node: # NÓ

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

# lista DUPLAMENTE ENCADEADA
class LinkedList:
    
    def  __init__(self):
        self.tail = None
        self.head = None
        self._size = 0

    def __len__(self): # retorna o TAMANHO da lista
        return self._size
    
    def _getnode(self, index): # retorna onde esta o PONTEIRO
        pointer = self.head

        for indice in range(index):
            if pointer == None:
                raise IndexError('O indice da lista está fora do range')
            else:
                pointer = pointer.next
        return pointer
    
    def index(self, elem): # retorna o indice do elemento
        pointer = self.head
        posiçao = 0

        while(pointer):
            if pointer.data == elem:
                return posiçao
            else:
                pointer.previous = pointer
                pointer = pointer.next
                posiçao = posiçao + 1

        return False # se nao encontrar o elemento

    def ADD(self, index, elem): # INSERE um elemento na lista
        ''' modo de uso primeiro passa o INDICE e depois passa o ELEMENTO
        lista.insert(0, 22)'''

        if index == 0:
            node = Node(elem)
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index - 1)
            node = Node(elem)
            node.next = pointer.next
            pointer.next = node

        self._size = self._size + 1

    def REM(self, elem): # REMOVE um elemento na lista
        if self.head == None:
            raise ValueError(f'"{elem}" nao está na lista')
        
        elif self.head.data == elem:
            self.head = self.head.next
            self._size = self._size - 1 
            return True

        else:
            previous = self.head
            pointer = self.head.next

            while(pointer):
                if pointer.data == elem:
                    previous.next = pointer.next
                    pointer.next = None
                previous = pointer
                pointer = pointer.next
            self._size = self._size - 1
            return True

    def EXIB(self): # vai printar a LISTA toda
        pointer = self.head
        while(pointer):
            print(str(pointer.data))
            pointer.previous = pointer
            pointer = pointer.next

    def FIND(self, elem): # vai localizar o elemento ja existente na lista e coloca-lo na posiçao 0
        if self.index(elem) == False: # verificando se o elemento está na lista
            pass
        else:
            self.REM(elem)
            self.ADD(0, elem)

# loop para ficar recebendo entrada   
double_list = LinkedList()
receber = True
while receber == True:
    input = input().split()
    if input[0] == 'END': # encerrar quando reber um END
        receber = False

    else:
        if input[0] == 'ADD':
            double_list.ADD(0, input[1])
        
        elif input[0] == 'REM':
            double_list.REM(input[1])

        elif input[0] == 'EXIB':
            double_list.EXIB()

        elif input[0] == 'FIND':
            double_list.FIND(input[1])
            
    del input
```

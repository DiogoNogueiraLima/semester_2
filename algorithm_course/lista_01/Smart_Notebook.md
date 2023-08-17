# Questão 1

## Caderno Inteligente

### Tempo limite: 1000ms

### Enunciado:
Um funcionário de uma papelaria em uma pequena cidade no interior de Essuatíni tem um problema. Ao receber a mais nova remessa de páginas de um caderno inteligente chamado Manual de Como Sobreviver em um País Que Ninguém Conhece, ele percebeu que as pilhas estavam bagunçadas, em ordens aparentemente caóticas. Por ser um caderno diferente, customizado para as necessidades de cada cliente, isso não seria estranho, pois as partes dos cadernos são muitas vezes sobrepostas, com capítulos dentro de outros, numa formatação bastante única para cada edição.

Infelizmente, o responsável pelo carregamento do produto perdeu a mão em uma curva e algumas pilhas se misturaram, causando uma grande confusão, e por isso as pilhas não são confiáveis. Agora, é responsabilidade desse funcionário conferir cada um dos cadernos para ver se eles estão com as capas na ordem correta, e, se não, onde está a primeira capa errada.

As capas têm dois tipos: frentes e versos, que funcionam como separadores e não são diferentes de um capítulo para outro. A única regra é que toda frente precisa ter um verso depois dela, não necessariamente imediatamente após, mas eventualmente. Para isso, nenhum verso pode aparecer sem que uma frente tenha o antecedido em algum momento. Se ao fim da pilha alguma frente não tiver o seu verso, esse também é um indicativo de que o caderno foi comprometido.

### Resumo do problema: 
Confira se todas as frentes (F) tem seus devidos versos (V) em uma ordem satisfatória. Toda frente precisa ter um verso depois dela, não necessariamente imediatamente após, mas eventualmente. Nenhum verso pode aparecer sem que uma frente tenha o antecedido em algum momento. E, atenção, uma pilha que tem a mesma quantidade de frentes e versos NÃO está necessariamente correta.

OBS: Strings vazias devem ser consideradas corretas.

### Input

A única linha de entrada é composta por uma string, que corresponde a pilha de capas manuseada pelo funcionário. A string é uma sequência de letras sem espaços ou vírgulas então elas, como VFVFFFVVFVFV.

### Output

Você deve produzir uma única linha de saída com a expressão “Correto.” caso a pilha seja bem formada, e “Incorreto, devido a capa na posição X.” caso contrário, onde X é a posição da primeira capa que interfere na integridade do caderno.




## Código de resolução:

```python
class Node: # NÓ

    def __init__(self, data):
        self.data = data
        self.next = None
        self.index = counter

class Queue:
    
    def  __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def __repr__(self):
        representation = ''
        pointer = self.first    
        while(pointer):
            representation = representation + str(pointer.data) + "\n"
            pointer = pointer.next
        return representation

    def __str__(self):
        return self.__repr__()


    def __len__(self): # RETORNA o TAMANHO da lista
        return self._size
    
    def push(self, elem): # INSERE um elemento na fila
        node = Node(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node

        self._size += 1

    def pop(self): # REMOVE o elemento do INICIO da fila
        if self._size > 0:
            elem = self.first.data
            self.first = self.first.next
            self._size -= 1
            return elem
        if self.first is not None:
            print(f'Incorreto, devido a capa na posição {self.first.index}.') # tem que dar o index de onde está o erro
            exit()
        else:
            print(f'Incorreto, devido a capa na posição {counter}.') # tem que dar o index de onde está o erro
            exit()

    def peek(self): # LÊ o elemento que está no INICIO da fila
        if self._size > 0:
            elem = self.first.data
            return elem
        raise IndexError

# recebendo a lista
lista = list(input())

# verificando cada elemento da lista
fila = Queue()
counter = 0
for elem in lista:
    if elem == 'F':
        counter += 1
        fila.push('frente')
        
    else:
        counter += 1
        fila.pop()
        

# verificando se o tamanho da fila é 0
if len(fila) == 0:
    print('Correto.')
else:
    print(f'Incorreto, devido a capa na posição {fila.first.index}.')

```

# Questão 1

## Sistema JUPAL

### Tempo limite: 
200 ms

### Enunciado:
Depois de tanto exercitar suas habilidades de programação no primeiro período de SI, chegou a hora de cursar a temida matéria de Algoritmos e Estruturas de Dados. Nessa peneira, você sabe que deverá se esforçar ao máximo para conseguir compreender os assuntos passados pelo professor e ainda realizar as atividades práticas no prazo estipulado. No entanto, todos sabem que a vida é uma experiência colaborativa, e para os estudantes isso não é diferente.

Para garantir que você e seus amigos tenham a experiência mais proveitosa possível, vocês decidem criar uma rede de ajuda mútua na qual os membros ajudam uns aos outros a passar pelos desafios que o período propõe. Para isso, você desenvolve um sistema para cadastrar cada um dos participantes dessa organização de maneira a gerenciar qual sua posição na árvore social e quais outros alunos cada um deve ajudar.

O sistema, chamado carinhosamente de JUPAL, possui três funções básicas: buscar, inserir e remover o nome de um integrante. Já no início da implementação do sistema, você percebe que a situação de alguns alunos “do topo” rapidamente se torna insustentável, pois muitas pessoas começam a depender deles, e o sistema se torna desbalanceado. Para agilizar esses processos e garantir a estabilidade emocional de todos os envolvidos, você decide utilizar uma estrutura famosa na engenharia de software que é perfeita para essa situação: a árvore balanceada AVL.

Como você bem sabe, árvores AVL fazem um balanceamento automático de suas folhas todas as vezes que é feita uma inserção ou remoção de maneira a sempre manter a altura de todas mais ou menos igual. Seguindo esse raciocínio, o sistema é capaz de manter todos os integrantes felizes, sem sobrecargas acontecendo de um lado ou de outro da árvore.

### DESCRIÇÃO DA IMPLEMENTAÇÃO

Você deve implementar uma árvore balanceada AVL, com um fator de balanceamento estável, tal que, para todos os nós da árvore: -1 <= f.b. <= 1. Para isso, estipula-se que o fator de balanceamento de cada dado nó é definido como: f.b(Nó) = altura(Nó->direita) - altura(Nó->esquerda). Alguns pontos importantes:

    A altura de um nó nulo é dada como 0;
    A altura de uma folha é 1;
    A altura de um nó qualquer é o valor máximo entre a altura do nó a sua direita e do nó a sua esquerda, somado 1.

#### Cada aluno da sua árvore deverá ser representado por uma string que corresponde ao seu nome, e a ordenação dos nós deverá seguir a prioridade padrão de strings (alfabética, lexicográfica).

#### ATENÇÃO: Já que estamos lidando com uma AVL, a inserção e a remoção serão feitas de maneira análoga à inserção e remoção de uma árvore de busca binária comum, mas após cada operação o programa deve verificar se aquele nó está balanceado de acordo com a relação exigida pela definição da estrutura. Caso não esteja, uma rotação deverá ser feita para que isso ocorra.

### Input
Seu programa deverá ler entradas repetidamente até que o comando FIM seja chamado. A lista de comandos possíveis é a seguinte:

    • INSERIR -nome- : Insere um nó com o valor -nome-

    • DELETAR -nome- : Deleta um nó com o valor -nome-

    • MINIMO : Retorna a string com o menor valor lexicográfico

    • MAXIMO : Retorna a string com o maior valor lexicográfico

    • ALTURA : Retorna a altura total da árvore, partindo da raiz

    • FIM : Finaliza o programa

### Output
Cada comando da lista anterior terá um retorno específico, como a seguir:

    • INSERIR <-nome>:

        Caso <-nome> não exista na árvore: <-nome> INSERIDO

        Caso <-nome> já exista na árvore: <-nome> JA EXISTE

    • DELETAR <-nome>:

        Caso <-nome> exista na árvore: <-nome> DELETADO

        Caso <-nome> não exista na árvore: <-nome> NAO ENCONTRADO

    • MINIMO:

        Caso a árvore não esteja vazia: MENOR: <-nome>

        Caso a árvore esteja vazia: ARVORE VAZIA

    • MAXIMO:

        Caso a árvore não esteja vazia: MAIOR: <-nome>

        Caso a árvore esteja vazia: ARVORE VAZIA

    • ALTURA:

        ALTURA: <-alturadaarvore>

    • FIM:

        Caso a árvore não esteja vazia: <-lista dos nós restantes da árvore, em ordem>

Caso a árvore esteja vazia: ARVORE VAZIA

## Código de resolução:
```python
'''
possui três funções básicas: buscar, inserir e remover o nome de um integrante
'''
ROOT = 'root'
class TreeNode: # criando a classe dos nos da arvore
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.data)
        
# Árvore Binária de Busca
class BinarySearchAVLTree:
    def __init__(self):
        self._size = 0
        self.root = None

    def height(self, node): # define a altura partindo de um no especifico da arvore, importante para a funçao do balance
        if node:
            return node.height
        else:
            return 0
    
    def final_height(self, node=None): # a altura final para o print da rrvoore
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

    def balance(self, node): # fazendo o balance da arovre

        if node is not None:
            return self.height(node.left) - self.height(node.right)

        else:
            return 0

    def rotacionar_direita(self, node): # girando para a direita
        left = node.left
        right_of_left = left.right
        left.right = node
        node.left = right_of_left

        # ajeitando a altura da arvore
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        left.height = 1 + max(self.height(left.left), self.height(left.right))

        return left

    def rotacionar_esquerda(self, node): # girando para a esquerda
        right = node.right
        left_of_right = right.left
        right.left = node
        node.right = left_of_right

        # ajeitando a altura da arvore
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        right.height = 1 + max(self.height(right.left), self.height(right.right))

        return right

    def insert(self, data):  # adicionando um novo elemento
        if self.root is not None:
            self.root = self._insert(data, self.root)
        else:
            print(f'{data} INSERIDO')
            self.root = TreeNode(data)

    def _insert(self, value, node=ROOT, count=0):
        if node is None:
            return TreeNode(value)
        
        # convertendo os nomes para inteiros para fazer a comparaçao
        valor_no = converter_para_num(node.data)
        if value is not int: # caso seja uma string
            num = converter_para_num(value)
        else:
            num = value

        if num == valor_no: # quando o no ja existir
            print(f'{value} JA EXISTE')
            return False
        elif num < valor_no: # se o valor adiconado for MENOR que o valor do no olhado
            node.left = self._insert(value, node.left, 1)
        else:                # se o valor adivionado for MAIOR que o valor do no olhado
            node.right = self._insert(value, node.right, 1)

        if count == 0: # verificando é a prinmeira chamada da inserçao para nao ficar varios prints iguais
            print(f'{value} INSERIDO')

        # atualizando o tamanho e a altura
        self._size += 1
        node.height = 1 + max(self.height(node.left), self.height(node.right))

        # verificando se ela tá balanceada
        balance = self.balance(node)
        if balance > 1 and num < converter_para_num(node.left.data):
            return self.rotacionar_direita(node)
        
        if balance > 1 and converter_para_num(node.left.data) < num:
            node.left = self.rotacionar_esquerda(node.left)
            return self.rotacionar_direita(node)
        
        if balance < -1 and converter_para_num(node.right.data) < num:
            return self.rotacionar_esquerda(node)
        
        if balance < -1 and num < converter_para_num(node.right.data):
            node.right = self.rotacionar_direita(node.right)
            return self.rotacionar_esquerda(node)
        
        return node

    def menor_no(self, node):
        if not node or not node.left:
            return node
        else:
            return self.menor_no(node.left)
    
    def remove(self, value):
        self.root = self._remove(value, self.root)

    def _remove(self, value, node=ROOT, count=0):
        if not node: # quando o elemento que quer remover NAO esta na lista
            print(f'{value} NAO ENCONTRADO')
            lista_remove.clear()
            return node
        
        if count == 0:
            lista_remove.append(1)

        # convertendo os nomes para inteiros para fazer a comparaçao
        valor_no = converter_para_num(node.data)
        if value is not int: # caso seja uma string
            num = converter_para_num(value)
        else:
            num = value
        
        if num < valor_no: # Se o valor for MENOR, desce à esquerda
            node.left = self._remove(value, node.left, 1)

        elif num > valor_no: # Se o valor for MAIOR, desce à direita
            node.right = self._remove(value, node.right, 1)

        else:  # Se não for nem menor, nem maior, ENCONTRAMOS! Vamos remover...
            if not node.left:
                substitute = node.right
                node = None
                return substitute
            elif not node.right:
                substitute = node.left
                node = None
                return substitute
            
            # Substituto é o sucessor do valor a ser removido
            substitute = self.menor_no(node.right)
            # Ao invés de trocar a posição dos nós, troca o valor
            node.data = substitute.data
            # Depois, remove o substituto da subárvore à direita
            node.right = self._remove(substitute.data, node.right, 1)

        # olhando se a arvore ta sem nada
        if not node:
            return node

        # atualizaçao do tamanho e altura
        self._size -= 1
        node.height = 1 + max(self.height(node.left), self.height(node.right))

        # vendo se ela ta balanceada
        balance = self.balance(node)

        if balance > 1 and self.balance(node.left) >= 0:
            return self.rotacionar_direita(node)
        
        if balance > 1 and self.balance(node.left) < 0:
            node.left = self.rotacionar_esquerda(node.left)
            return self.rotacionar_direita(node)
        
        if balance < -1 and self.balance(node.right) <= 0:
            return self.rotacionar_esquerda(node)
        
        if balance < -1 and self.balance(node.right) > 0:
            node.right = self.rotacionar_direita(node.right)
            return self.rotacionar_esquerda(node)

        return node
    
    def inorder_traversal(self, node=None): # faz o percurso em ordem simetrica
        if node is None:
            node = self.root

        if node.left:
            self.inorder_traversal(node.left)
        lista_print.append(node)

        if node.right:
            self.inorder_traversal(node.right)

    def min(self, node=None):

        if node is None:
            print('ARVORE VAZIA')
            return False

        if node == ROOT:
            node = self.root

        while node.left:
            node = node.left

        print(f'MENOR: {node.data}')
        return 
    
    def max(self, node=None):

        if node is None:
            print('ARVORE VAZIA')
            return False
        if node == ROOT:
            node = self.root

        while node.right:
            node = node.right

        print(f'MAIOR: {node.data}')
        return

# funçao para converter string para numero
def converter_para_num(string):

    decimal = 0
    count = 0

    for char in string:

        decimal *= 1000
        decimal += ord(char)
        count += 1

        if count == 4:
            break

    return decimal

# COMEÇANDO O CODIGO EM SI
lista_remove = []
lista_print = []
arvore = BinarySearchAVLTree() 
receber = True
while receber == True:

    input = input().split()

    if input[0] == 'FIM': # encerrar quando reber um FIM
        receber = False

        if arvore.root is not None:
            arvore.inorder_traversal()
            for i in range(len(lista_print) - 1):
                print(f'{lista_print[i]} ', end='')
            print(lista_print[len(lista_print) - 1], end='')

        else: # vai printar ARVORE VAZIA se nao tiver ngm
            print('ARVORE VAZIA')

    else:
        if input[0] == 'INSERIR':
            arvore.insert(input[1])

        elif input[0] == 'DELETAR':
            arvore.remove(input[1])
            if len(lista_remove) != 0:
                print(f'{input[1]} DELETADO')

        elif input[0] == 'MINIMO':
            arvore.min(arvore.root)

        elif input[0] == 'MAXIMO':
            arvore.max(arvore.root)

        elif input[0] == 'ALTURA':
            print(f'ALTURA: {arvore.final_height()}')

        else:
            print('PELO SPORT NADAAAAAAAAA')
            print('TUDOOOOOOOOOOOOOOOOOOOOO')
            print('CAZA CAZA CAZA')

    del input


''' Exemplo de entrada:
DELETAR Fabinho
INSERIR Fabinho
DELETAR Fabinho
INSERIR Chico
DELETAR Chico
INSERIR Jorginho
MAXIMO
INSERIR Juba
INSERIR Wanderson
INSERIR Kayke
DELETAR Juba
INSERIR Vagner
INSERIR Pedro
ALTURA
MINIMO
FIM


'''
```

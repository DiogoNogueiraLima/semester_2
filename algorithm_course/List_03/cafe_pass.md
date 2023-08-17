# Questão 1

## Café Pass

### Tempo limite: 
1000 ms

### Enunciado:
O Centro de Informática estava enfrentando um problema sério com a cafeteira de sua sala de convivência. Alguns alunos estavam consumindo quantidades excessivas de café, deixando pouco para os demais. Para resolver o problema, o time de desenvolvimento do Helpdesk CIn-UFPE, liderado por Charles do Helpdesk, decidiu criar um sistema de autorização experimental chamado "CaféPass" para validar se uma aluna(o) pode acessar a cafeteira da sala de convivência na semana.

#### Funcionamento:

Toda Segunda o sistema carrega CPFs dos alunos e forma um array a partir de seus dígitos multiplicado por 10 :

    ex.: 72290379050 => [70, 20, 20, 90, 0, 30, 70, 90, 0, 50, 0]

Caso o CPF tenha dígitos repetidos, então deve-se reduzir esse array somando os valores duplicados:

    ex.: [70, 20, 20, 90, 0, 30, 70, 90, 0, 50, 0] => [140, 40, 180, 0, 30, 50]

Por último, é gerado um número aleatório (Magic Number) entre 30 e 990 para cada CPF. Dessa forma, se a soma de dois elementos distintos do array final for igual ao número aleatório, então a aluna(o) ganha permissão de acessar a sala de convivência para usar a cafeteira na semana.

    Pode usar lista (Python List)
    Não pode usar dicionário (Python dict)
    Atenção com o uso excessivo de trechos com O(nˆ2)
    Obrigatório usar Tabela Hash

### Input
    N - Onde N é o número de operações da entrada

Várias linhas com a seguinte informação:

    CPF MN - Calcula autorização considerando um CPF e um (magic number) MN.

Limites de Input

    len(CPF) = 11
    30 <= MN <= 990

### Output


## Código de resolução:
```python
# funçao para pegar cada numero da entrada
def soma(cpf):
    separador = list(cpf)
    for cada_num in separador: # separando cada numero do cpf e somando 1 a cada apariçao dele e colocando ele na posiçao na lista de remoçao
        chave_mod[int(cada_num)] += 1

    count = 0
    for cada_lista in chave_mod:
        if cada_lista == 0: # se nenhum numero com o valor de cada num foi adicionado, a funçao passa, para nao criar listas sem nada
            pass

        else: # se tiver o numero, adiciona na lista da soma o: valor * 10 * a quantidade de vezes que ele aparece
            soma = cada_lista * 10 * count
            sum_list.append(soma)

        count += 1

def soma_suprema(comparaçao):
    for i in range(len(sum_list)):
        for j in range(i+1, len(sum_list)):
            soma = sum_list[i] + sum_list[j]
            if int(comparaçao) == int(soma): # se o numero comparado estiver for igual ao da soma
                return True
    return False

# começando o codigo em si
qnt_entrada = int(input())
for i in range(qnt_entrada):
    # ajeitando os valores a cada loop e recebendo a nova entrada
    chave_mod =  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    sum_list = []
    entrada = input().split()

    # começando os calculos
    soma(entrada[0]) # cpf
    boleano = soma_suprema(entrada[1]) # somando todas as possiveis combinaçoes de soma dentro das listas
    if boleano == True:
        print('UP Permission')
    else:
        print('NOT Permission')

    del entrada
```

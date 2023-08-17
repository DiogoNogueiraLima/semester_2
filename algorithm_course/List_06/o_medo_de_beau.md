# Questão 1

## O Medo de Beau

### Tempo limite: 
100 ms

### Enunciado:
É de conhecimento geral que Ari Aster é um grande cineasta. Diretor, roteirista e produtor americano, Aster ganhou reconhecimento por seus filmes de terror psicológico perturbadores e complexos, rapidamente se tornando um ícone do gênero. Após o sucesso de crítica e público de Hereditary (2018) e Midsommar (2019), Aster volta às salas de cinema com o aguardado longa-metragem Beau Is Afraid, e fãs de todo o mundo estão ansiosos para prestigiar a nova obra do diretor.

No entanto, apesar de seu prestígio, BIA foi lançado em meio a um cenário bastante desafiador. Com o sucesso mundial de Super Mario Bros, poucas são as sessões disponibilizadas pelas redes de cinema para que seja feita a exibição de um filme indie de terror psicológico. Além disso, os fãs do gênero ainda tem que passar pelo dilema de qual filme assistir, já que a continuação do clássico Evil Dead também foi lançada no mês de abril.

Nesse cenário, as pessoas que se dispõem a sair de casa de 21h para assistir uma das duas únicas sessões do filme encontram salas relativamente vazias. Com isso, elas sentem-se na liberdade de sentar onde quiserem nas fileiras do cinema, e grupos de amigos acabam se separando se assim desejarem.

##### Considere uma "sala infinita" na qual sempre haverão lugares vazios disponíveis.

##### Comece considerando casos que todas as pessoas ficam sozinhas e termine com todas sentando juntas.

##### Ignore permutações!

### Input
Você receberá apenas um número inteiro n, onde n se refere ao número de pessoas que compraram ingressos para uma determinada sessão do filme.

### Output
O output deverá retornar todas as maneiras que as pessoas pedem se separar para assistir ao filme, da seguinte maneira:

###### Uma sessão com <n> pessoas pode ter sua audiência nos seguintes subgrupos:

###### [a, a, a..]

###### [a, a..]

###### [a]

Onde a 1 <= a <= n e a vírgula separa os subgrupos com lugares vazios. Observe os exemplo para entender os detalhes de como as possibilidades devem ser impressas.

## Código de resolução:
```python
# criando a funçao recursiva para saber todos os grupos possiveis
def grupos(soma):
    if soma == num_pessoas:
        print(formacao)
        return

    for i in range(1, num_pessoas - soma + 1):
        if not formacao or i >= formacao[-1]:
            formacao.append(i)
            grupos(soma + i)
            formacao.pop()


# recebendo a entrada
num_pessoas = int(input())

# output
formacao = []
print(f'Uma sessão com {num_pessoas} pessoas pode ter sua audiência nos seguintes subgrupos:')
grupos(0)
```

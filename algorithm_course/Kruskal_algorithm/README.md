## Contexto do projeto:

Era necessário gerar uma árvore geradora mínima, para isso precisava saber com quantas arestas e quanto eram os custos das arestas para que fosse formado o menor número de árvores (se possível apenas uma só) possível para conectar maior número de nós com o menor número de arestas possíveis e essas conexões de arestas feitas com o menor peso possível. A partir dessa base de dados, entretanto não se sabia como realizar essa tarefa de forma que fosse otimizada, nesse ponto utilizamos do algoritmo de árvore geradora mínima de Kruskal, algoritmo que é conhecido por resolver problemas como esse de forma otimizada, para realizar essa tarefa e resolver esse problema.

## sobre a base de dados:

Sobre a base de dados bio-SC-LC ela é um conjunto de grafos direcionados que representam um modelo de regulação genética em leucócitos e células estromais. Essa base de dados foi coletada pelo laboratório de sistemas biológicos da Universidade de Stanford, nos Estados Unidos. Cada grafo representa um conjunto de interações entre proteínas que regulam a expressão genética em células. As proteínas são representadas como nós do grafo e as interações entre elas são representadas como arestas. Essa base de dados é útil para estudos de biologia molecular e celular, pois fornece informações sobre as interações entre proteínas em células. Além disso, essa base de dados também pode ser usada para testar e desenvolver algoritmos de análise de redes complexas.

## O que é o algoritmo de Kruskal:

O algoritmo de Kruskal é um algoritmo de grafos que encontra a árvore geradora mínima de um grafo conectado e ponderado. O objetivo é encontrar o subconjunto das arestas do grafo que formam uma árvore que inclui todos os vértices, onde a soma dos pesos das arestas é a menor possível. O algoritmo de Kruskal começa com um conjunto de árvores que contém apenas um vértice cada. Em seguida, ele ordena todas as arestas em ordem crescente de peso e, em seguida, insere cada uma delas em ordem na árvore, verificando se a adição da aresta não criará um ciclo. O algoritmo continua adicionando arestas à árvore até que todos os vértices estejam conectados. Em resumo, o algoritmo de Kruskal é usado para encontrar a árvore geradora mínima em um grafo ponderado, que é muito útil em muitos problemas práticos, como em redes de comunicação, sistemas de transporte e distribuição de energia.

## Como foi feito o desenvolvimento
O projeto foi feito completamente na linguagem de programação python e utilizei de duas bibliotecas para facilitar a vizualização de alguns processos (pandas e sys).

## Bibliotecas utilizadas
Nós utilizamos de duas bibliotecas, para facilitar o processo de análise do banco de dados utilizamos do pandas, que ja é uma biblioteca conhecida em python para análise de dados, e para podermos utilizar da função exit() no notebook utilizamos da função sys que possibilita a utilização de várias funções pro sistema

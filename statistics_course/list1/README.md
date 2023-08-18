# Enunciado
Gere k sequências de números aleatórios cada uma de tamanho n e as ordene, usando algoritmos de ordenação tais como o QuickSort, HeapSort, BubbleSort (ou algum outro de sua preferência). Analise os k resultados encontrados para cada algoritmo. Note que a variável de interesse é tempo de execução para cada algoritmo. Crie um estudo experimental e descreva como foi realizado o planejamento (CAMPOS, 2012). (2.0) Exemplo de resultado:

![Screenshot](ultima.png)

Como exemplo mostrado na Tabela, temos k sequências (k_1, k_2 e k_n) cada uma com 200, 500 e 450 números aleatórios (ou pseudoaleatórios) gerados. Os resultados (em tempos de execução) estão listados na tabela.


Primeiramente, gostaria de comunicar que utilizei os seguintes algoritmos para a realização do experimento: Quicksort, Bubblesort e o Timsort (algoritmo padrão de ordenação proveniente do python). Comecei criando uma função no python utilizando o método “import random” para a geração de “k” listas, todas com “n” números pseudo-aleatórios. Após isso, fui atrás de criar e testar uma função para realizar a checagem para verificar se as listas geradas aleatoriamente estavam realmente desordenadas. Depois, fui atrás dos algoritmos bubblesort e quicksort na internet. Após isso, criei um laço de repetição para cada algoritmo ordenar cada lista e guardar o valor de quanto tempo levou para ordenar cada uma das listas por meio do “import time" (fazendo o tempo final que terminou de executar o algoritmo menos o tempo ao iniciar o uso do algoritmo) num dicionário. Depois de guardar os valores dos tempos de execução de cada uma das listas de cada um dos algoritmos, criei uma função para calcular a média aritmética, o tempo mínimo, o tempo máximo e o desvio padrão de cada um dos algoritmos. Então coloquei o k=2 e o n=6 e fui depurando para ver se estava tudo funcionando certo. Após a certificação da corretude de todas as partes do código, decidi colocar os valores para aparecerem em milissegundos com duas casas decimais de aproximação. Com o código pronto fui “colocar” tudo para rodar com “k” e “n” maiores, coloquei k=30 e n=6.500, para ter uma maior precisão nos dados. Como conclusão, podemos perceber a eficiência impressionantemente excelente do Timsort, o bom desempenho do quicksort e a resolução extremamente lenta do Bubblesort.

PS: O algoritmo “DEFAULT” é o algoritmo padrão do python (Timsort)
Legendas: 
min: mínimo
max: máximo
avg: média aritmética
stdev: desvio padrão

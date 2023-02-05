def _bubble_sort_list(list):
    sorted_list = list.copy()

    #loops para percorrer o array
    for final in range(len(sorted_list), 0, -1):
        for atual in range(0, final - 1):
            #comparacao elemento atual se for menor que o proximo elemento
            if (sorted_list[atual] > sorted_list[atual + 1]):
                sorted_list[atual], sorted_list[atual + 1] = sorted_list[atual + 1], sorted_list[atual]
                
    return sorted_list

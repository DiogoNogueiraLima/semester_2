'''
This program collects and shows sort algorithms statitcs
'''

'''
Imports
'''

import random
import os
import time
from collections import namedtuple
from statistics import mean, stdev
from quicksort import _quick_sort_list
from bubblesort import _bubble_sort_list

'''
Global defintions
'''

Statistic = namedtuple('Statistic', 'min max avg stdev')

_K = 30  # the num of lists to sort
_N = 6500  # number of elements in each list

_SORT_ALGORITHMS = ['DEFAULT', 'QUICKSORT', 'BUBBLESORT']

'''
_sort_lists_time = {
    'default': [T0, T1, ...., T(K-2), T(K-1)]
    'bubble': [T0, T1, ...., T(K-2), T(K-1)]
    'quick': [T0, T1, ...., T(K-2), T(K-1)]
}
'''
_sort_lists_time = {}

'''
_sort_lists_statistics = {
    'default': Statistic(min, max, average, stddev)
    'bubble': Statistic(min, max, average, stddev)
    'quick': Statistic(min, max, average, stddev)
}
'''
_sort_lists_statistics = {}

'''
Private functions
'''

def _generate_lists(k, n):
    '''
    Generates a list of 'n' random numbers
    '''
    lists = []
    for j in range(0, k):
        list = []
        for i in range(0, n):
            random_number = random.randint(0, 10000)
            list.append(random_number)
        lists.append(list)
    return lists

def _collect_statistic(sortname):
    ellapesed_times = _sort_lists_time[sortname]
    min_time = min(ellapesed_times)
    max_time = max(ellapesed_times)
    avg_time = mean(ellapesed_times)
    stdev_time = stdev(ellapesed_times)

    statistic = Statistic(min_time, max_time, avg_time, stdev_time)

    _sort_lists_statistics[sortname] = statistic

def _print_statistic(sortname):
    statistic = _sort_lists_statistics[sortname]
    print(sortname + ":")
    print("\t" + "min: " + str(round(statistic.min, 2)) + " ms")
    print("\t" + "max: " + str(round(statistic.max, 2)) + " ms")
    print("\t" + "avg: " + str(round(statistic.avg, 2)) + " ms")
    print("\t" + "stdev: " + str(round(statistic.stdev, 2)) + " ms")

def _check_orderd_list(list):
    for i in range(1, len(list)):
        if list[i] < list[i-1]:
            return False
    return True

def _sort_list(algorithm, list):
    if algorithm == 'DEFAULT':
        return _default_sort_list(list)
    elif algorithm == 'QUICKSORT':
        return _quick_sort_list(list)
    elif algorithm == 'BUBBLESORT':
        return _bubble_sort_list(list)
    else:
        print("Unknown algorithm")
        os.abort()

def _default_sort_list(list):
    sorted_list = list.copy()
    sorted_list.sort()
    return sorted_list

def _print_statistics():
    print("\n\n")
    for algorithm in _SORT_ALGORITHMS:
        _collect_statistic(algorithm)
        _print_statistic(algorithm)

'''
Public functions
'''

def compare(k, n):
    _sort_lists_time.clear()
    for algorithm in _SORT_ALGORITHMS:
        _sort_lists_time[algorithm] = []

    lists = _generate_lists(k, n)
    for algorithm in _SORT_ALGORITHMS:
        print(f"starting '{algorithm}'")
        
        for list in lists:
            if _check_orderd_list(list):
                print("I'm a bad programmer. My check is buggy")
                os.abort()

            start_time = time.time()
            sorted_list = _sort_list(algorithm, list)
            end_time = time.time()
            ellapsed_time = (end_time - start_time) * 1000

            _sort_lists_time[algorithm].append(ellapsed_time)

            if not _check_orderd_list(sorted_list):
                print(f"I'm a bad programmer. My sorting algorithm '{algorithm}' is buggy, or my check is buggy")
                os.abort()
    
    _print_statistics()

    

if __name__ == "__main__":
    compare(_K, _N)

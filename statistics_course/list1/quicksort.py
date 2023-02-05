def _quick_sort_list(list):
    """Sort the list by using quicksort."""
    
    sorted_list = list.copy()
    less = []
    equal = []
    greater = []

    if len(sorted_list) > 1:
        pivot = sorted_list[0]

        for x in sorted_list:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)

        # Don't forget to return something!
        return _quick_sort_list(less) + equal + _quick_sort_list(greater)  # Just use the + operator to join lists
    
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your list, just return the list.
        return sorted_list

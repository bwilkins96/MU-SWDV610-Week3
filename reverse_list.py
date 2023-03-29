# SWDV 610: Data Structures and Algorithms
# Recursive function that reverses a list

def reverse_list(lst, start=0, stop=None):
    """Reverses the order of a list from start to stop indexes"""
    if stop == None: stop = len(lst) - 1

    if stop - start >= 1:
        lst[start], lst[stop] = lst[stop], lst[start]
        reverse_list(lst, start+1, stop-1)

    return lst

if __name__ == '__main__':
    test_1 = reverse_list([1, 2, 3, 4, 5])   
    test_2 = reverse_list([14, 17, 21, 257, 4, 51])
    test_3 = reverse_list([1, 2])
    test_4 = reverse_list([])
    
    print(test_1)          # -> [5, 4, 3, 2, 1]
    print(test_2)          # -> [51, 4, 257, 21, 17, 14]
    print(test_3)          # -> [2, 1]
    print(test_4)          # -> []

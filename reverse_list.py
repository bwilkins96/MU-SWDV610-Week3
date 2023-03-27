# SWDV 610: Data Structures and Algorithms
# Recursive function that reverses a list

def reverse_list(lst, start=0, stop=None):
    '''Reverses the order of a list and accepts optional start and stop arguments'''
    if not stop: stop = len(lst) - 1

    if stop - start > 1:
        lst[start], lst[stop] = lst[stop], lst[start]
        reverse_list(lst, start+1, stop-1)

if __name__ == '__main__':
    test_1 = [1,2,3,4,5]
    test_2 = [14, 17, 21, 257, 4]
    test_3 = []

    reverse_list(test_1)   
    reverse_list(test_2)
    reverse_list(test_3) 
    
    print(test_1)          # -> [5, 4, 3, 2, 1]
    print(test_2)          # -> [4, 257, 21, 17, 14]
    print(test_3)          # -> []

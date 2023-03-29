# SWDV 610: Data Structures and Algorithms
# Recursive function that finds the minimum and maximum values in a sequence

def min_max(seq, idx=0, min=float('inf'), max=float('-inf')):
    """Returns the min and max values of a sequence"""    
    if idx == len(seq):
        if len(seq) == 0: 
            min, max = None, None    

        return (min, max)

    val = seq[idx]
    if val < min: min = val
    if val > max: max = val

    return min_max(seq, idx+1, min, max)

if __name__ == '__main__':
    test_1 = min_max([1, 2, 3, 4, 5])
    test_2 = min_max([6, 7, -513, 8, 9, 20000, 10])
    test_3 = min_max([5])
    test_4 = min_max([])
    
    print(test_1)          # -> (1, 5)
    print(test_2)          # -> (-513, 20000)
    print(test_3)          # -> (5, 5)
    print(test_4)          # -> (None, None)
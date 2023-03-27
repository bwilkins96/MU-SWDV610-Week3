# Recursive 'solution' to the tower of hanoi puzzle
# Doesn't solve the problem at large height values, because it currently can't!

def move_tower(height, from_pole, to_pole, with_pole):
    '''Prints instructions for the tower of hanoi puzzle'''
    if height >= 1:
        move_tower(height-1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height-1, with_pole, to_pole, from_pole)

def move_disk(from_pole, to_pole):
    '''Helper function for move_tower'''
    print('Move disk from', from_pole, 'to', to_pole)

if __name__ == '__main__':
    move_tower(3, 'A', 'B', 'C')
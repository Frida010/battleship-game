# Import random package to be able to create random integers

import random

# Create square board
def build_board(dims):
    return [['0' for count in range(dims)] for count in range(dims)]

build_board(4)

[['0','0','0','0'],
['0','0','0','0'],
['0','0','0','0'],
['0','0','0','0']]

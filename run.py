# Import random package to be able to create random integers

import random

# Create random ships on game board
def create_ship():
    return random.randint(0, 5), random.randint(0, 5)

def play_game():
    game_board = [["O", "O", "O", "O", "O"],
                  ["O", "O", "O", "O", "O"],
                  ["O", "O", "O", "O", "O"],
                  ["O", "O", "O", "O", "O"],
                  ["O", "O", "O", "O", "O"]]

    for b in game_board:
        print(*b)

    
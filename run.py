# Import random package to be able to create random integers

import random

# Create random ships on game board
def create_ship():
    return random.randint(0, 5), random.randint(0, 5)


print("Welcome to the battleship game!"
       "\nYour task is to find and destroy all the ships on the map.\n")

print("""\nIntroductions:
\nYou have 10 ammo and there are 3 hidden ships on the map.
In order to hit them, you have to enter the numbers for that location. 
For example:
The first row and first column, you write 1 and 1.
Good luck!\n""")

def play_game():
    game_board = [["O", "O", "O", "O", "O"],
                  ["O", "O", "O", "O", "O"],
                  ["O", "O", "O", "O", "O"],
                  ["O", "O", "O", "O", "O"],
                  ["O", "O", "O", "O", "O"]]

    for b in game_board:
        print(*b)

    ship1 = create_ship()
    ship2 = create_ship()
    ship3 = create_ship()
    ships_left = 3
    ammo = 10

    
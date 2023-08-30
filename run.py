# Import random package to be able to create random integers
import random


# Create random ships on game board
def create_ship():
    return random.randint(0, 5), random.randint(0, 5)


# Asks user to play again or quit game.
def play_again():
    try_again = input("Want to play again? <Y>es or <N>o? ->: ")
    if try_again == "y":
        play_game()
    else:
        print("Goodbye!")
        return


# Instruction and welcome message.
print("""Welcome to the battleship game!
       \nYour task is to find and destroy all the ships on the map.""")

print("""\nIntroductions:
\nYou have 10 ammo and there are 3 hidden ships on the map.
In order to hit them, you have to enter the numbers for that location.
For example:
The first row and first column, you write 1 and 1.
Good luck!\n""")


# Game board
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

    while ammo:
        try:
            # Tells the user to enter number between 1-5.
            row = int(input("Enter a row number between 1 and 5 ->: "))
            column = int(input("Enter a column number between 1 and 5 ->: "))
        except ValueError:
            # Notify the user if letters were inserted insted of number
            print("Only enter numbers!")
            continue

        # Checks if users number is in the right range, else tell the user.
        if row not in range(1, 6) or column not in range(1, 6):
            print("\nThe number must be between 1 and 5!")
            continue

        # Reducing number to desired index
        row = row - 1
        column = column - 1
        # Checks if user already selected that spot.
        if game_board[row][column] == "-" or game_board[row][column] == "X":
            print("\nYou have already shoot that place!\n")
            continue
        # Checks if user hit a ship.
        elif (row, column) == ship1 or (row, column) == ship2 or (row, column) == ship3:
            print("\nBOOM! You hit a ship! You were rewared a new ammo!\n")
            game_board[row][column] = "X"
            ships_left -= 1
            # Congratulate the user when all ships are gone
            if ships_left == 0:
                print("Congratulation! You won!")
                play_again()
        # Tell the user if they miss and subtract ammo by one.
        else:
            print("\nYou missed!\n")
            game_board[row][column] = "-"
            ammo -= 1

        for b in game_board:
            print(*b)

        # Tells the user how much ammo and ships is left.
        print(f"Ammo left: {ammo} | Ships left: {ships_left}")

    play_again()


if __name__ == "__main__":
    play_game()

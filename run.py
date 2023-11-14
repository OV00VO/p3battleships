# Credit: Code is based on inspiration from Code Institute and several other collected sources. 
# To create a working a game logic in this game most of the code had to be modified.

import random

MESSAGE_LENGTH = 80

class Board:
    def __init__(self, size):
        self.size = size
        self.cells = [['_' for _ in range(size)] for _ in range(size)]
        self.ships_remaining = 0

    def place_ship(self, ship_length, orientation):
        attempts = 0
        max_attempts = 100  # Set a maximum number of attempts to avoid an infinite loop

        while attempts < max_attempts:
            start_row = random.randint(0, self.size - 1)
            start_col = random.randint(0, self.size - 1)

            if self.check_valid_ship_placement(start_row, start_col, orientation, ship_length):
                for i in range(ship_length):
                    if orientation == 'H':
                        self.cells[start_row][start_col + i] = '#'
                    else:
                        self.cells[start_row + i][start_col] = '#'
                self.ships_remaining += 1
                break

            attempts += 1

        if attempts == max_attempts:
            raise RuntimeError("Failed to place the ship after the maximum number of attempts. Please check the board size and ship placement logic.")

    def check_valid_ship_placement(self, row, col, orientation, ship_length):
        for i in range(ship_length):
            if orientation == 'H':
                if col + i >= self.size or self.cells[row][col + i] != '_':
                    return False
            else:
                if row + i >= self.size or self.cells[row + i][col] != '_':
                    return False
        return True

    def attack(self, row, col):
        if row < 0 or row >= self.size or col < 0 or col >= self.size:
            return False  # Invalid attack coordinates

        if self.cells[row][col] == '#':
            self.cells[row][col] = 'O'
            self.ships_remaining -= 1
            return True  # Hit
        elif self.cells[row][col] == '_':
            self.cells[row][col] = 'X'
            return False  # Miss

    def has_remaining_ships(self):
        return self.ships_remaining > 0

def clear_screen():
    print('\n' * 100)

def display_board(player_board, computer_board, player_hits, player_misses, player_guesses, computer_guesses):
    clear_screen()
    print("-" * MESSAGE_LENGTH)
    print(f"{NAME}'s Hits: {player_hits}\t\t\t\t\t\tComputer's Hits: {board_size - computer_board.ships_remaining}")
    print(f"{NAME}'s Misses: {player_misses}\t\t\t\t\t\tComputer's Misses: {player_misses}")

    print("\n" + f"{NAME}'s Board\t\t\t\t\t\tComputer's Board")
    for player_row, computer_row in zip(player_board.cells, computer_board.cells):
        print('|', ' |'.join(str(cell) for cell in player_row), '|', '\t\t\t', '|', ' |'.join(str(cell) if cell == 'O' or cell == 'X' else '_' for cell in computer_row), '|')

    if player_guesses:
        print("\nPlayer's Guesses:")
        for guess in player_guesses:
            print(guess)

    if computer_guesses:
        print("\nComputer's Guesses:")
        for guess in computer_guesses:
            print(guess)

def get_user_input(prompt, is_integer=False):
    while True:
        try:
            user_input = input(prompt)
            if is_integer:
                return int(user_input)
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid value.")

def play_round(player_board, computer_board, board_size):
    player_hits = 0
    player_misses = 0
    player_score = 0
    player_guesses = set()
    computer_guesses = set()

    while True:
        display_board(player_board, computer_board, player_hits, player_misses, player_guesses, computer_guesses)

        player_row = get_user_input(f"{NAME}, enter row to attack 1 - {board_size}: ", is_integer=True) - 1
        player_col = get_user_input(f"{NAME}, enter column to attack 1 - {board_size}: ", is_integer=True) - 1

        if not (0 <= player_row < board_size and 0 <= player_col < board_size):
            player_guesses.add(f"{NAME} guessed ({player_row + 1}, {player_col + 1}) and that was an Invalid Attack!")
            continue

        player_guess = (player_row, player_col)
        if player_guess in player_guesses or player_board.cells[player_row][player_col] == 'O' or player_board.cells[player_row][player_col] == 'X':
            player_guesses.add(f"{NAME} guessed ({player_row + 1}, {player_col + 1}) and that was a Hit/Miss! Please choose different ones.")
            continue

        player_guesses.add(f"{NAME} guessed ({player_row + 1}, {player_col + 1}) and that was a ")

        if computer_board.attack(player_row, player_col):
            player_hits += 1
            player_guesses.add("Hit!")
            player_score += 1
        else:
            player_misses += 1
            player_guesses.add("Miss!")

            if not computer_board.has_remaining_ships():
                display_board(player_board, computer_board, player_hits, player_misses, player_guesses, computer_guesses)
                print("-" * MESSAGE_LENGTH)
                print(f"All of Computer's ships have been sunk! {NAME} wins!")
                print(f"Score: {NAME} - {player_score}")
                break

        # Computer's turn
        valid_attacks = [(row, col) for row in range(board_size) for col in range(board_size) if player_board.cells[row][col] == '_']

        computer_guess = random.choice(list(set(valid_attacks) - computer_guesses))
        computer_guesses.add(computer_guess)

        computer_guess_text = f"Computer guessed ({computer_guess[0] + 1}, {computer_guess[1] + 1}) and that was a "
        computer_guess_text += "Hit!" if player_board.attack(computer_guess[0], computer_guess[1]) else "Miss!"

        if not player_board.has_remaining_ships():
            display_board(player_board, computer_board, player_hits, player_misses, player_guesses, computer_guesses)
            print("-" * MESSAGE_LENGTH)
            print(f"All of {NAME}'s ships have been sunk! Computer wins!")
            print(f"Score: Computer - {board_size - computer_board.ships_remaining}")
            break

        computer_guesses.add(computer_guess_text)

if __name__ == "__main__":
    clear_screen()
    print("-" * MESSAGE_LENGTH)
    print("Welcome to the fun game of Battleships!")
    print("Select board size up to 10 by 10")
    print("Top left corner is your 1st row and column")
    print("Select how many battleships you would like of maximum 10 different")
    print("-" * MESSAGE_LENGTH)

    NAME = get_user_input("Please enter your name: ")
    board_size = get_user_input("Enter board size (5-10): ", is_integer=True)

    player_board = Board(board_size)
    computer_board = Board(board_size)

    num_ships = get_user_input("Enter the number of ships (1-10): ", is_integer=True)
    for _ in range(num_ships):
        player_board.place_ship(random.randint(2, 4), random.choice(['H', 'V']))
        computer_board.place_ship(random.randint(2, 4), random.choice(['H', 'V']))

    play_round(player_board, computer_board, board_size)

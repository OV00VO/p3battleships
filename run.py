# Credits and Refereces are mentioned below and in README.md.
# There is also credit given to Code Institue course material.
# In most cases are the code modified to fit the aims for the game itself.

import random

MESSAGE_LENGTH = 40

class Board:
    def __init__(self, size):
        self.size = size
        self.cells = [['_' for _ in range(size)] for _ in range(size)]
        self.ships_remaining = 0
        
    # Reference: https://www.geeksforgeeks.org/python-programming-examples/
    def place_ship(self, ship_length, orientation):
        attempts = 0
        max_attempts = 100
        max_ships = min(self.size, 4)

        while attempts < max_attempts:
            start_row = random.randint(0, self.size - 1)
            start_col = random.randint(0, self.size - 1)

            if orientation == 'H' and start_col + ship_length <= self.size:
                valid_placement = all(self.cells[start_row][start_col + i] == '_' for i in range(ship_length))
            elif orientation == 'V' and start_row + ship_length <= self.size:
                valid_placement = all(self.cells[start_row + i][start_col] == '_' for i in range(ship_length))
            else:
                valid_placement = False

            if valid_placement:
                for i in range(ship_length):
                    if orientation == 'H':
                        self.cells[start_row][start_col + i] = '#'
                    else:
                        self.cells[start_row + i][start_col] = '#'
                self.ships_remaining += 1
                break

            attempts += 1

        if attempts >= max_attempts:
            print("Warning: Placing ships took too long. Consider picking a smaller number of ships.")
            raise RuntimeError("Failed to place the ship after the maximum number of attempts. Please check the board size and ship placement logic.")
    
    # Reference: https://www.geeksforgeeks.org/python-programming-examples/
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
            return False

        if self.cells[row][col] == '#':
            self.cells[row][col] = 'O'
            self.ships_remaining -= 1
            return True
        elif self.cells[row][col] == '_':
            self.cells[row][col] = 'X'
            return False

    def has_remaining_ships(self):
        return self.ships_remaining > 0
        
# Reference: https://stackoverflow.com/questions/273192/how-to-clear-console-in-python
def clear_screen():
    print('\n' * 100)

# Reference https://pythondex.com/python-battleship-game
def display_board(player_name, player_board, computer_name, computer_board, player_hits, player_misses, player_guesses, computer_guesses):
    clear_screen()
    print("-" * MESSAGE_LENGTH)

    print(f"{player_name}'s Board of Battleships:".ljust(MESSAGE_LENGTH // 2))
    print('-' * MESSAGE_LENGTH)
    for player_row in player_board.cells:
        print('|', ' |'.join(str(cell).ljust(2) for cell in player_row).ljust(MESSAGE_LENGTH // 4 - 1), '|')

    print('-' * MESSAGE_LENGTH)
    print(f"{computer_name}'s Board of Battleships:".ljust(MESSAGE_LENGTH // 2))
    print('-' * MESSAGE_LENGTH)
    for computer_row in computer_board.cells:
        print('|', ' |'.join(str(cell).ljust(2) if cell == 'O' or cell == 'X' else '_'.ljust(2) for cell in computer_row).ljust(MESSAGE_LENGTH // 4 - 1), '|')

    print('-' * MESSAGE_LENGTH)
    print(f"\n{player_name}'s Status:".ljust(MESSAGE_LENGTH // 2))
    print(f"{player_name}'s Hits: {player_hits}".ljust(MESSAGE_LENGTH // 2))
    print(f"{player_name}'s Misses: {player_misses}".ljust(MESSAGE_LENGTH // 2))

    if player_guesses:
        print('-' * MESSAGE_LENGTH)
        print("\nPlayer's Guess:")
        print(player_guesses[-1].ljust(MESSAGE_LENGTH // 2))

    if computer_guesses:
        print('-' * MESSAGE_LENGTH)
        print("\nComputer's Guess:")
        print(computer_guesses[-1].ljust(MESSAGE_LENGTH // 2))

    print('-' * MESSAGE_LENGTH)
    print(f"\n{computer_name}'s Status:".ljust(MESSAGE_LENGTH // 2))
    print(f"{computer_name}'s Hits: {board_size - computer_board.ships_remaining}".ljust(MESSAGE_LENGTH // 2))
    print(f"{computer_name}'s Misses: {player_misses}".ljust(MESSAGE_LENGTH // 2))

    print("-" * MESSAGE_LENGTH)

def get_user_input(prompt, is_integer=False, valid_range=None):
    while True:
        try:
            user_input = input(prompt)
            if is_integer:
                value = int(user_input)
                if valid_range and not valid_range[0] <= value <= valid_range[1]:
                    raise ValueError(f"Please enter a value between {valid_range[0]} and {valid_range[1]}.")
                return value
            return user_input
        except ValueError as e:
            print(f"Error: {e}")

# Reference https://pythondex.com/python-battleship-game
def play_round(player_board, computer_board, board_size, player_name, computer_name):
    player_hits = 0
    player_misses = 0
    player_score = 0
    player_guesses = []
    computer_guesses = []

    while True:
        display_board(player_name, player_board, computer_name, computer_board, player_hits, player_misses, player_guesses, computer_guesses)

        while True:
            player_row = get_user_input(f"{player_name}, enter row to attack 1 - {board_size}: ", is_integer=True, valid_range=(1, board_size)) - 1
            player_col = get_user_input(f"{player_name}, enter column to attack 1 - {board_size}: ", is_integer=True, valid_range=(1, board_size)) - 1

            if player_board.cells[player_row][player_col] in ('O', 'X'):
                print(f"You've already attacked the coordinates ({player_row + 1}, {player_col + 1}). Please choose different coordinates, {player_name}.")
            else:
                break

        player_guess_text = f"{player_name} guessed ({player_row + 1}, {player_col + 1}) and that was a "
        player_guess_text += "Hit!" if computer_board.attack(player_row, player_col) else "Miss."

        if player_board.attack(player_row, player_col):
            player_hits += 1
            player_guesses.append(player_guess_text)
            player_score += 1
        else:
            player_misses += 1
            player_guesses.append(player_guess_text)

            if not computer_board.has_remaining_ships():
                display_board(player_name, player_board, computer_name, computer_board, player_hits, player_misses, player_guesses, computer_guesses)
                print("-" * MESSAGE_LENGTH)
                print(f"All of {computer_name}'s ships have been sunk! {player_name} wins!")
                print(f"Score: {player_name} - {player_score}")
                break

        valid_attacks = [(row, col) for row in range(board_size) for col in range(board_size) if player_board.cells[row][col] == '_']

        if not valid_attacks:
            print("No more valid coordinates to guess. Computer skips its turn.")
        else:
            computer_guess = random.choice(list(set(valid_attacks) - set(computer_guesses)))
            hit_or_miss = "Hit!" if player_board.attack(computer_guess[0], computer_guess[1]) else "Miss!"
            computer_guesses.append(f"{computer_name} guessed ({computer_guess[0] + 1}, {computer_guess[1] + 1}) and that was a {hit_or_miss}")

        if not player_board.has_remaining_ships():
            display_board(player_name, player_board, computer_name, computer_board, player_hits, player_misses, player_guesses, computer_guesses)
            print("-" * MESSAGE_LENGTH)
            print(f"All of {player_name}'s ships have been sunk! {computer_name} wins!")
            print(f"Score: {computer_name} - {board_size - computer_board.ships_remaining}")
            break

# Reference https://pythondex.com/python-battleship-game
if __name__ == "__main__":
    clear_screen()
    print("-" * MESSAGE_LENGTH)
    print("Welcome to the fun game of Battleships!")
    print("Select board size up to 10 by 10")
    print("Top left corner is first row and column")
    print("Select how many battleships you would\nlike of a maximum of 10 different ones.")
    print("-" * MESSAGE_LENGTH)

    player_name = get_user_input("Please enter your name: ")
    computer_name = "Computer"
    board_size = get_user_input("Enter board size (5-10): ", is_integer=True, valid_range=(5, 10))

    player_board = Board(board_size)
    computer_board = Board(board_size)

    while True:
        num_ships = get_user_input("Enter the number of ships (1-10): ", is_integer=True, valid_range=(1, 10))
        if num_ships > board_size:
            print("Sorry, the number of ships cannot be greater than the board size. Please choose a smaller number of ships.")
        else:
            break

    for _ in range(num_ships):
        player_board.place_ship(random.randint(2, 4), random.choice(['H', 'V']))
        computer_board.place_ship(random.randint(2, 4), random.choice(['H', 'V']))

    play_round(player_board, computer_board, board_size, player_name, computer_name)

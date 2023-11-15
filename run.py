# Credits and References mentioned below and in README.md.
# Credit given to Code Institute course curriculum and material.
# In most cases, the code is modified for the game itself.

import random

MESSAGE_LENGTH = 40


class Board:
    def __init__(self, size):
        self.size = size
        self.cells = [['_' for _ in range(size)] for _ in range(size)]
        self.ships_remaining = 0

# Reference/Credit:
# https://www.geeksforgeeks.org/python-programming-examples/

    def place_ship(self, ship_length, orientation):
        available_spaces = sum(row.count('_') for row in self.cells)
        max_attempts = min(available_spaces, self.size * 5)
        attempts = 0

        while attempts < max_attempts:
            start_row = random.randint(0, self.size - 1)
            start_col = random.randint(0, self.size - 1)

            is_valid_h_placement = (
                orientation == 'H' and
                start_col + ship_length <= self.size and
                all(self.cells[start_row][start_col + i] == '_'
                    for i in range(ship_length))
            )

            is_valid_v_placement = (
                orientation == 'V' and
                start_row + ship_length <= self.size and
                all(self.cells[start_row + i][start_col] == '_'
                    for i in range(ship_length))
            )

            valid_placement = is_valid_h_placement or is_valid_v_placement

            if valid_placement:
                for i in range(ship_length):
                    if orientation == 'H':
                        self.cells[start_row][start_col + i] = '#'
                    else:
                        self.cells[start_row + i][start_col] = '#'
                self.ships_remaining += 1
                break

            attempts += 1

        if attempts >= max_attempts and ship_length > 2:
            print("Warning! Consider picking a smaller number of ships.")
            attempts = 0
            ship_length -= 1

# Reference/Credit:
# https://www.geeksforgeeks.org/python-programming-examples/

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
        if not (0 <= row < self.size) or not (0 <= col < self.size):
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

# Reference/Credit:
# https://stackoverflow.com/questions/273192/how-to-clear-console-in-python


def clear_screen():
    print('\n' * 100)

# Reference/Credit:
# https://pythondex.com/python-battleship-game


def display_board(player, player_board, computer, computer_board,
                  player_hit, player_miss, player_guess, computer_guess):
    clear_screen()
    print("-" * MESSAGE_LENGTH)

    print(f"{player}'s Battleships:".ljust(MESSAGE_LENGTH // 2))
    print('-' * MESSAGE_LENGTH)
    for player_row in player_board.cells:
        print(
            '|', ' |'.join(str(cell).ljust(2) for cell in player_row)
            .ljust(MESSAGE_LENGTH // 4 - 1), '|'
        )

    print('-' * MESSAGE_LENGTH)
    print(f"{computer}'s Battleships:".ljust(MESSAGE_LENGTH // 2))
    print('-' * MESSAGE_LENGTH)
    for computer_row in computer_board.cells:
        print(
            '|', ' |'.join(
                str(cell).ljust(2) if cell == 'O' or cell == 'X' else '_'
                .ljust(2) for cell in computer_row
            ).ljust(MESSAGE_LENGTH // 4 - 1), '|'
        )

    print('-' * MESSAGE_LENGTH)
    print(f"\n{player}'s Status:".ljust(MESSAGE_LENGTH // 2))
    print(f"{player}'s Hits: {player_hit}".ljust(MESSAGE_LENGTH // 2))
    print(f"{player}'s Misses: {player_miss}".ljust(MESSAGE_LENGTH // 2))

    if player_guess:
        print('-' * MESSAGE_LENGTH)
        print("\nPlayer's Guess:")
        print(player_guess[-1].ljust(MESSAGE_LENGTH // 2))

    if computer_guess:
        print('-' * MESSAGE_LENGTH)
        print("\nComputer's Guess:")
        print(computer_guess[-1].ljust(MESSAGE_LENGTH // 2))

    print('-' * MESSAGE_LENGTH)
    print(f"\n{computer}'s Status:".ljust(MESSAGE_LENGTH // 2))
    print(
        f"{computer}'s Hit: {board_size - computer_board.ships_remaining}"
        .ljust(MESSAGE_LENGTH // 2))
    print(f"{computer}'s Miss: {player_miss}".ljust(MESSAGE_LENGTH // 2))

    print("-" * MESSAGE_LENGTH)


def get_user_input(prompt, is_integer=False, v_range=None, player=None):
    while True:
        try:
            user_input = input(prompt)
            if is_integer:
                value = int(user_input)
                if v_range and not v_range[0] <= value <= v_range[1]:
                    raise ValueError(f"{v_range[0]} and {v_range[1]}.")
                return value
            return user_input
        except ValueError as e:
            print(f"Error: {e}")
            if is_integer:
                print(f"Please, use only scope numbers for your coordinates.")

# Reference/Credit:
# https://pythondex.com/python-battleship-game


def play_round(player_board, computer_board, board_size, player, computer):
    player_hit = 0
    player_miss = 0
    player_score = 0
    player_guess = []
    computer_guess = []

    while True:
        display_board(player, player_board, computer, computer_board,
                      player_hit, player_miss, player_guess, computer_guess)

        while True:
            player_row = get_user_input(
                f"{player}, enter row to attack 1 - {board_size}: ",
                is_integer=True, v_range=(1, board_size)
            ) - 1
            player_col = get_user_input(
                f"{player}, enter column to attack 1 - {board_size}: ",
                is_integer=True, v_range=(1, board_size)
            ) - 1

            if player_board.cells[player_row][player_col] in ('O', 'X'):
                print(
                    f"You've already attacked this one ({player_row + 1}, "
                    f"{player_col + 1}), Select another position, {player}."
                )
            else:
                break

        player_guess_text = (
            f"{player} guessed ({player_row + 1}, {player_col + 1}) "
            f"that was a "
        )

        if player_board.attack(player_row, player_col):
            player_hit += 1
            player_guess.append(player_guess_text + "Hit!")
            player_score += 1
        else:
            player_miss += 1
            player_guess.append(player_guess_text + "Miss!")

            if not computer_board.has_remaining_ships():
                display_board(
                    player, player_board, computer, computer_board,
                    player_hit, player_miss, player_guess, computer_guess)
                print("-" * MESSAGE_LENGTH)
                print(
                    f"All of {computer}'s ships sunk! {player} wins!")
                print(f"Score: {player} - {player_score}")
                break

        valid_attacks = [
            (row, col)
            for row in range(board_size)
            for col in range(board_size)
            if player_board.cells[row][col] == '_']

        if not valid_attacks:
            print(
                "No more valid coordinates to guess. Computer skips its turn.")
        else:
            computer_guess_tuple = random.choice(
                list(set(valid_attacks) - set(computer_guess)))
            hit_or_miss = "Hit!" if player_board.attack(
                computer_guess_tuple[0], computer_guess_tuple[1]) else "Miss!"
            computer_guess.append(
                f"{computer} guessed ({computer_guess_tuple[0] + 1}, "
                f"{computer_guess_tuple[1] + 1}) that was a {hit_or_miss}")

        if not player_board.has_remaining_ships():
            display_board(player, player_board, computer, computer_board,
                          player_hit, player_miss,
                          player_guess, computer_guess)
            print("-" * MESSAGE_LENGTH)
            print(
                f"All of {player}'s ships sunk! {computer} wins!")
            score_prefix = f"Score: {computer} - "
            score_suffix = f"{board_size - computer_board.ships_remaining}"
            print(score_prefix.ljust(MESSAGE_LENGTH // 2) + score_suffix)

            break

# Reference/Credit:
# https://www.geeksforgeeks.org/python-programming-examples/


if __name__ == "__main__":
    clear_screen()
    print("-" * MESSAGE_LENGTH)
    print("Welcome to the fun game of Battleships!")
    print("Select board size from 5 to 10")
    print("Top left corner is the first row and column")
    print("Select the number of battleships from 1 to 10.")
    print("-" * MESSAGE_LENGTH)

    player = get_user_input("Please enter your name: ")
    computer = "Computer"
    board_size = get_user_input(
        "Enter board size (5-10): ", is_integer=True, v_range=(5, 10))

    player_board = Board(board_size)
    computer_board = Board(board_size)

    while True:
        num_ships = get_user_input(
            "Enter the number of ships (1-10): ", is_integer=True,
            v_range=(1, 10))
        if num_ships > board_size:
            print(
                "Sorry, the number of ships cannot be greater than the board.")
        else:
            break

    for _ in range(num_ships):
        player_board.place_ship(
            random.randint(2, 4), random.choice(['H', 'V']))
        computer_board.place_ship(
            random.randint(2, 4), random.choice(['H', 'V']))

    play_round(player_board, computer_board, board_size, player, computer)


_range=None):
    while True:
        user_input = input(prompt)
        if is_integer:
            try:
                user_input = int(user_input)
                if valid_range is None or (valid_range[0] <= user_input <= valid_range[1]):
                    return user_input
                else:
                    print(f"Please enter a number between {valid_range[0]} and {valid_range[1]}.")
            except ValueError:
                print("Please enter a valid integer.")
        else:
            return user_input

def play_round(player_board, computer_board, board_size, player_name, computer_name):
    player_hits = 0
    player_misses = 0
    player_guesses = []
    computer_guesses = []

    while True:
        display_board(player_name, player_board, computer_name, computer_board, player_hits, player_misses, player_guesses, computer_guesses)

        print(f"\n{player_name}, it's your turn!")
        player_row = get_user_input("Enter the row to attack (1-{}): ".format(board_size), is_integer=True, valid_range=(1, board_size)) - 1
        player_col = get_user_input("Enter the column to attack (1-{}): ".format(board_size), is_integer=True, valid_range=(1, board_size)) - 1

        while not player_board.check_valid_ship_placement(player_row, player_col, 'H', 1):
            print("You've already attacked this location. Please choose a different set of coordinates.")
            player_row = get_user_input("Enter the row to attack (1-{}): ".format(board_size), is_integer=True, valid_range=(1, board_size)) - 1
            player_col = get_user_input("Enter the column to attack (1-{}): ".format(board_size), is_integer=True, valid_range=(1, board_size)) - 1

        player_guess_text = f"{player_name} guessed ({player_row + 1}, {player_col + 1}) and that was a "
        player_guess_text += "Hit!" if computer_board.attack(player_row, player_col) else "Miss."

        if player_board.attack(player_row, player_col):
            player_hits += 1
            player_guesses.append(player_guess_text)
        else:
            player_misses += 1
            player_guesses.append(player_guess_text)

            if not computer_board.has_remaining_ships():
                display_board(player_name, player_board, computer_name, computer_board, player_hits, player_misses, player_guesses, computer_guesses)
                print("-" * MESSAGE_LENGTH)
                print(f"All of {computer_name}'s ships have been sunk! {player_name} wins!")
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
            break

# Reference: https://pythondex.com/python-battleship-game
if __name__ == "__main__":
    clear_screen()
    print("-" * MESSAGE_LENGTH)
    print("Welcome to the fun game of Battleships!")
    print("Select board size up to 10 by 10")
    print("Top left corner is the first row and column")
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
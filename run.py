import random

MESSAGE_LENGTH = 80

class Board:
    def __init__(self, size):
        self.size = size
        self.cells = [['_' for _ in range(size)] for _ in range(size)]
        self.ships_remaining = 0
      
      def place_ship(self, ship_length, orientation):
        while True:
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

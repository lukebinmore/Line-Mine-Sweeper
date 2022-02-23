# region Imports
from random import randint

# endregion

# region Global Variables
WINDOW_WIDTH = 80
MINE_VAL = -1
# endregion

# region Game Board Class
class Board:
    """
    Minesweeper game class.
    """

    size = 7
    mines = 5
    grid_hidden = []
    grid_visable = []

    def __init__(self, grid_size):
        self.size = grid_size
        self.create_grids()
        self.create_mines()
        self.set_numbers()

    def create_grids(self):
        """
        Creates both the hidden and visable grids as nested lists.
        Fills the newly created hidden grid with 0's.
        Fills the newly created visable grid with spaces.
        """

        self.grid_hidden = [
            [0 for column in range(self.size)] for row in range(self.size)
        ]
        self.grid_visable = [
            [" " for column in range(self.size)] for row in range(self.size)
        ]

    def draw_board(self):
        """
        Adds stylings to each row of the visable grid.
        Prints out visable grid row by row, using center_line function.
        """

        heading_top = (
            "".join(["|  " + str(i + 1) + "  " for i in range(self.size)]) + "|"
        )
        print(center_line(heading_top))
        print()

        for i, row in enumerate(self.grid_hidden):
            new_line = ""

            if i == 0:
                new_line = "\u203E  "
                new_line = (
                    new_line
                    + "".join(["|\u203E\u203E\u203E\u203E\u203E" for cell in row])
                    + "|   "
                )
            else:
                new_line = "   "
                new_line = new_line + "".join(["|     " for cell in row]) + "|   "

            print(center_line(new_line))

            new_line = str(i + 1) + "  "
            new_line = (
                new_line + "".join(["|  " + str(cell) + "  " for cell in row]) + "|   "
            )
            print(center_line(new_line))

            new_line = "_  "
            new_line = new_line + "".join(["|_____" for cell in row]) + "|   "
            print(center_line(new_line))

    def create_mines(self):
        """
        Uses randint from the random library to create randomly located mines in the hidden grid.
        """

        for _ in range(self.mines):
            while True:
                new_row = randint(0, self.size - 1)
                new_column = randint(0, self.size - 1)

                if self.grid_hidden[new_row][new_column] != MINE_VAL:
                    self.grid_hidden[new_row][new_column] = MINE_VAL
                    break

    def set_numbers(self):
        """
        Sets the correct numbers for each cell in the hidden grid.
        Checks each cell's neighboring cells for mines.
        Increases cell value if it is next to a mine.
        """
        for row in range(self.size):
            for col, cell in enumerate(self.grid_hidden[row]):
                if cell == MINE_VAL:
                    continue

                if row > 0:
                    if col > 0 and self.grid_hidden[row - 1][col - 1] == MINE_VAL:
                        self.grid_hidden[row][col] += 1

                    if self.grid_hidden[row - 1][col] == MINE_VAL:
                        self.grid_hidden[row][col] += 1

                    if (
                        col < self.size - 1
                        and self.grid_hidden[row - 1][col + 1] == MINE_VAL
                    ):
                        self.grid_hidden[row][col] += 1

                if col > 0 and self.grid_hidden[row][col - 1] == MINE_VAL:
                    self.grid_hidden[row][col] += 1
                if col < self.size - 1 and self.grid_hidden[row][col + 1] == MINE_VAL:
                    self.grid_hidden[row][col] += 1

                if row < self.size - 1:
                    if col > 0 and self.grid_hidden[row + 1][col - 1] == MINE_VAL:
                        self.grid_hidden[row][col] += 1

                    if self.grid_hidden[row + 1][col] == MINE_VAL:
                        self.grid_hidden[row][col] += 1

                    if (
                        col < self.size - 1
                        and self.grid_hidden[row + 1][col + 1] == MINE_VAL
                    ):
                        self.grid_hidden[row][col] += 1


# endregion

# region Functions
def center_line(line):
    """
    Centers the given string based on the width of the terminal,
    set with the global WIDTH perameter.
    """

    new_line_spaces = int((WINDOW_WIDTH - len(line)) / 2)
    return "".join([" " for space in range(new_line_spaces)]) + line


# endregion

# region Main
def main():
    """
    Main function
    """

    game = Board(7)
    game.draw_board()


main()
# endregion

# region Imports

# endregion

# region Global Variables
WINDOW_WIDTH = 80
# endregion

# region Game Board Class
class Board:
    """
    Minesweeper game class.
    """

    size = 7
    grid_hidden = []
    grid_visable = []

    def __init__(self, grid_size):
        self.size = grid_size
        self.create_grids()

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

        for i, row in enumerate(self.grid_visable):
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


# endregion

# region Functions
def center_line(line):
    """
    Centers the given string based on the width of the terminal, set with the global WIDTH perameter.
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

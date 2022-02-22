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
            [" " for column in range(self.size) for row in range(self.size)]
        ]
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
    print(center_line("testpoisdjfpoksdfo"))

main()
# endregion

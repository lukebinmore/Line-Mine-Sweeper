# region Imports

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

# region Main
def main():
    """
    Main function
    """

    game = Board(7)
    print(game.grid_hidden)
    print(game.grid_visable)


main()
# endregion

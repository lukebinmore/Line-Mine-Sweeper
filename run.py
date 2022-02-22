# region Imports

# endregion

# region Game Board Class
class Board:
    """Minesweeper game class"""

    size = 7
    grid_hidden = []
    grid_visable = []

    def __init__(self, grid_size):
        """A"""

        self.size = grid_size
        self.create_grids()

    def create_grids(self):
        """A"""

        self.grid_hidden = [
            [0 for column in range(self.size)] for row in range(self.size)
        ]
        self.grid_visable = [
            [" " for column in range(self.size) for row in range(self.size)]
        ]


# endregion

# region Main
def main():
    """Main function"""

    game = Board(7)
    print(game.grid_hidden)
    print(game.grid_visable)


main()
# endregion

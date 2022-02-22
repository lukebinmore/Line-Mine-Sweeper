# region Imports

# endregion

# region Game Board Class
class Board:
    """Minesweeper game class"""

    size = 7
    grid_hidden = []
    grid_visable = []

    def __init__(self, grid_size):
        self.size = grid_size


# endregion

# region Main
def main():
    """Main function"""

    game = Board(7)


main()
# endregion

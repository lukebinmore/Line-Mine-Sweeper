# region Imports
import os
from random import randint
from readchar import readkey
from colorama import init, Fore

# endregion

# region Global Variables
TITLE = "  LINE MINE SWEEPER!!  "
WINDOW_WIDTH = 80
MINE_VAL = -1
DEFAULT_SETTINGS = [6, 10]
# endregion

# region Game Board Class
class Board:
    """
    Minesweeper game class.
    """

    size = 0
    mines = 0
    grid_hidden = []
    grid_visable = []

    def __init__(self, settings):
        self.size = settings[0]
        self.mines = settings[1]
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

        print_title()

        heading_top = (
            "".join(["|  " + str(i + 1) + "  " for i in range(self.size)]) + "|"
        )
        print(set_color(center_line(heading_top), Fore.CYAN))

        for i, row in enumerate(self.grid_visable):
            new_line = ""

            if i == 0:
                new_line = set_color("\u203E ", Fore.CYAN, True)
                new_line = (
                    new_line
                    + "".join(["|\u203E\u203E\u203E\u203E\u203E" for cell in row])
                    + "|   "
                )
            else:
                new_line = "  "
                new_line = new_line + "".join(["|     " for cell in row]) + "|  "

            print(center_line(new_line))

            new_line = set_color(str(i + 1) + " ", Fore.CYAN, True)
            new_line = (
                new_line + "".join(["|  " + str(cell) + "  " for cell in row]) + "|  "
            )
            print(center_line(new_line))

            new_line = set_color("_ ", Fore.CYAN, True)
            new_line = new_line + "".join(["|_____" for cell in row]) + "|  "
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

    def user_input(self):
        """
        User input manager for game.
        Takes user's input, and runs appropriate function based on what is received.
        """

        selection = ["", "", ""]

        print(center_line("\b\bPlease enter coordinates: "), end="", flush=True)

        try:
            selection[0] = readkey()

            if selection[0].isdigit():
                selection[0] = int(selection[0])
            else:
                raise ValueError(f"INVALID INPUT: {selection[0]} is not a number.")

            if selection[0] < 1 or selection[0] > self.size:
                raise ValueError(f"INVALID INPUT: {selection[0]} is not on the board.")

            print(str(selection[0]) + ":", end="", flush=True)
            selection[0] = selection[0] - 1
            selection[1] = readkey()

            if selection[1].isdigit():
                selection[1] = int(selection[1])
            else:
                raise ValueError(f"INVALID INPUT: {selection[1]} is not a number.")

            if selection[1] < 1 or selection[1] > self.size:
                raise ValueError(f"INVALID INPUT: {selection[1]} is not on the board.")

            print(str(selection[1]) + ":", end="", flush=True)
            selection[1] = int(selection[1]) - 1
            selection[2] = readkey()

            if selection[2].lower() == "f":
                selection[2] = True
            elif selection[2] == "\r":
                selection[2] = False
            else:
                raise ValueError(
                    f"INVALID INPUT: {selection[2]} is not 'f/F' or ENTER."
                )

            return selection
        except ValueError as error:
            error_message(error)

    def update_board(self, selection):
        """
        Checks if coordinates have already been revealed,
        if not updates the visable board with the user's inputted coordinates.
        """

        row, col = selection[0], selection[1]
        flag = selection[2]
        value_hidden = self.grid_hidden[row][col]
        value_visable = self.grid_visable[row][col]

        if value_visable == " " or value_visable == "F":
            if flag:
                self.grid_visable[row][col] = (
                    "F" if self.grid_visable[row][col] == " " else " "
                )
            elif value_hidden == 0:
                self.update_neighbours(row, col)
            else:
                self.grid_visable[row][col] = value_hidden

        else:
            error_message(
                f"INVALID INPUT: {row + 1}:{col + 1} has already been already revealed!"
            )

    def update_neighbours(self, row, col):
        """
        Checks neighbouring cells for 0 values,
        Addes them to the visable board if they are zero's adjasent to the starting cell.
        """

        if self.grid_hidden[row][col] == 0 and self.grid_visable[row][col] == " ":
            self.grid_visable[row][col] = 0

            if row > 0 and col > 0:
                self.update_neighbours(row - 1, col - 1)

            if row > 0:
                self.update_neighbours(row - 1, col)

            if row > 0 and col < self.size - 1:
                self.update_neighbours(row - 1, col + 1)

            if col > 0:
                self.update_neighbours(row, col - 1)

            if col < self.size - 1:
                self.update_neighbours(row, col + 1)

            if row < self.size - 1 and col > 0:
                self.update_neighbours(row + 1, col - 1)

            if row < self.size - 1:
                self.update_neighbours(row + 1, col)

            if row < self.size - 1 and col < self.size - 1:
                self.update_neighbours(row + 1, col + 1)

    def check_game_over(self):
        """
        Checks if the game should end.
        Checks if all mines have been flagged and all other cells have been revealed.
        """

        if -1 in (cell for row in self.grid_visable for cell in row):
            draw_game_results(False)
            return False

        if " " in (cell for row in self.grid_visable for cell in row):
            return True

        flag_count = 0
        for row in self.grid_visable:
            for cell in row:
                flag_count += 1 if cell == "F" else 0

        if flag_count == self.mines:
            draw_game_results(True)
            return False

        return False


# endregion

# region Functions
def center_line(line):
    """
    Centers the given string based on the width of the terminal,
    set with the global WIDTH perameter.
    """
    new_line_spaces = int((WINDOW_WIDTH - len(line)) / 2)
    return "".join([" " for space in range(new_line_spaces)]) + line


def menu():
    """
    Menu generator.
    Creates a menu of options, and uses user input to set settings for game.
    Returns settings as list.
    """

    settings = [setting for setting in DEFAULT_SETTINGS]

    while True:
        print_title()
        print()
        print(center_line("Welcome to Line Mine Sweeper!!"))
        print(center_line("Please select your desired settings below:"))
        print()
        print(center_line("1:"))
        print(center_line(f"Set Game Size - Current: {settings[0]}X{settings[0]}"))
        print()
        print(center_line("2:"))
        print(center_line(f"Set Mine Count - Current: {settings[1]}"))
        print()
        print(center_line("ENTER:"))
        print(center_line("Start Game!"))
        print()
        if settings[1] > settings[0] * settings[0]:
            print(center_line("!!!MINE COUNT TOO HIGH!!!"))
            print(center_line("Please increase grid size, or decrease mine count!"))
            print()

        try:
            print(center_line("\bPlease enter your selection: "), end="", flush=True)
            selection = readkey()

            if selection == "1":
                print_title()
                print()
                print(center_line("Please enter your desired grid size."))
                print(
                    center_line(
                        "Please enter a single number for grid size. (E.G. 5 = 5X5)"
                    )
                )
                print(center_line("Minimum = 2 | Maximum = 7"))
                print(center_line(f"Current = {settings[0]} X {settings[0]}"))
                print()

                print(
                    center_line("\bPlease enter your selection: "), end="", flush=True
                )
                selection = readkey()

                if selection.isdigit():
                    selection = int(selection)
                else:
                    raise ValueError(f"INVALID INPUT: {selection} is not a number.")

                if selection < 2:
                    raise ValueError(f"INVALID INPUT: {selection} is too low.")
                elif selection > 7:
                    raise ValueError(f"INVALID INPUT: {selection} is too high.")
                else:
                    settings[0] = selection

            elif selection == "2":
                print_title()
                print()
                print(center_line("Please enter your desired mine count."))
                print(
                    center_line(
                        "Please enter a single or double digit number. (E.G. 5 OR 20)"
                    )
                )
                print(
                    center_line(f"Minimum = 1 | Maximum = {settings[0] * settings[0]}")
                )
                print(center_line(f"Current Mines = {settings[1]}"))
                print()

                selection = input(center_line("Please enter your selection: "))

                if selection.isdigit():
                    selection = int(selection)
                else:
                    raise ValueError(f"INVALID INPUT: {selection} is not a number.")

                if selection < 1:
                    raise ValueError(f"INVALID INPUT: {selection} is too low.")
                elif selection > settings[0] * settings[0]:
                    raise ValueError(f"INVALID INPUT: {selection} is too high.")
                else:
                    settings[1] = selection

            elif selection == "\r":
                if settings[1] > settings[0] * settings[0]:
                    raise ValueError("ERROR: Cannot start game. Too many mines.")
                else:
                    return settings
            else:
                raise ValueError(f"UNKNOWN INPUT: {selection} is not an option.")
        except ValueError as error:
            error_message(error)

    return settings


def error_message(error):
    """
    Formats and displays an error the program has encountered.
    Takes in the error as a string, and adjusts the terminal display to show it.
    """

    print_title()
    print()
    print(set_color(center_line("ERROR HAS BEEN ENCOUNTERED!!!"), Fore.YELLOW))
    print()
    print(set_color(center_line(repr(str(error))), Fore.YELLOW))
    print()
    print(center_line("Please press any key to continue... "), end="", flush=True)
    readkey()


def print_title():
    """
    Clears the current screen.
    Prints title to terminal.
    Uses TITLE constant for title, and fills rest in with hashtags.
    """

    clear_terminal = lambda: os.system("cls" if os.name in ["nt", "dos"] else "clear")
    clear_terminal()

    new_line_spaces = int((WINDOW_WIDTH - len(TITLE)) / 2)
    new_line_section = "".join(["#" for space in range(new_line_spaces)])
    print(set_color(new_line_section + TITLE + new_line_section, Fore.GREEN))


def draw_game_results(winner):
    """
    Draws the game results screen,
    Displays Game Over if a mine was hit,
    Displays You Win! if all mines were found.
    """

    print_title()
    print()

    if winner:
        print(
            set_color(
                center_line("█████████████████████████████████████████████████"),
                Fore.GREEN,
            )
        )
        print(
            set_color(
                center_line("█▄─█▀▀▀█─▄█▄─▄█▄─▀█▄─▄█▄─▀█▄─▄█▄─▄▄─█▄─▄▄▀█░█░█░█"),
                Fore.GREEN,
            )
        )
        print(
            set_color(
                center_line("██─█─█─█─███─███─█▄▀─███─█▄▀─███─▄█▀██─▄─▄█▄█▄█▄█"),
                Fore.GREEN,
            )
        )
        print(
            set_color(
                center_line("▀▀▄▄▄▀▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▀▄▀▄▀"),
                Fore.GREEN,
            )
        )

        print()
        print(center_line("YEAH!!!"))
        print()
        print(center_line("You Found All The Mines!"))
        print()
        print(center_line("You Won! :)"))
        print()
        print(center_line("Press Any Key To Continue..."), end="", flush=True)
    else:
        print(
            set_color(
                center_line(
                    "█████▀████████████████████████████████████████████████████"
                ),
                Fore.RED,
            )
        )
        print(
            set_color(
                center_line(
                    "█─▄▄▄▄██▀▄─██▄─▀█▀─▄█▄─▄▄─███─▄▄─█▄─█─▄█▄─▄▄─█▄─▄▄▀█░█░█░█"
                ),
                Fore.RED,
            )
        )
        print(
            set_color(
                center_line(
                    "█─██▄─██─▀─███─█▄█─███─▄█▀███─██─██▄▀▄███─▄█▀██─▄─▄█▄█▄█▄█"
                ),
                Fore.RED,
            )
        )
        print(
            set_color(
                center_line(
                    "▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▀▀▄▄▄▄▀▀▀▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▀▄▀▄▀"
                ),
                Fore.RED,
            )
        )

        print()
        print(center_line("OH NO!!!"))
        print()
        print(center_line("You Hit A Mine!"))
        print()
        print(center_line("Better Luck Next Time :)"))
        print()
        print(center_line("Press Any Key To Continue..."), end="", flush=True)

    readkey()


def set_color(text, color, shift=False):
    """
    Adds supplied color index to supplied string.
    """
    
    if shift: return f"          {color}{text}{Fore.RESET}"

    return f"{color}{text}{Fore.RESET}"


# endregion

# region Main
def main():
    """
    Main function
    """

    while True:
        game = Board(menu())

        while game.check_game_over():
            game.draw_board()

            user_input = game.user_input()

            if not user_input is None:
                game.update_board(user_input)


init()
main()
# endregion

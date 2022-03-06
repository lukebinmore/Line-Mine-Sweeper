# Line Mine Sweeper - [Live Site](https://line-mine-sweeper.herokuapp.com/)

**Line Mine Sweeper** is a web terminal based Minesweeper game, deployed using the Code Institute mock terminal, via Heroku.

User's use coordinates and flags to reveal the location of all mines in the grid, without detonating any of them,
flagging all of the mines and revealing all non-mine cells to win.

![Am I Responsive](media/am-i-responsive.png)

## Table of Contents
- [Line Mine Sweeper - Live Site](#line-mine-sweeper---live-site)
  - [Table of Contents](#table-of-contents)
  - [How to Play](#how-to-play)
  - [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#future-features)
  - [Data Model](#data-model)
  - [Library's/Modules](#librarysmodules)
  - [Testing](#testing)
  - [Deployment](#deployment)
  - [Credits](#credits)

## How to Play

Line Mine Sweeper is a terminal version of the game Minesweeper, with the same rules and goals, with the only difference being the use of entered coordinates instead of a graphical interface.

In this game, the pleyer selects their board size and the quantity of mines they would likee to have to find.
At this point, they player also has the option of showing the instructions for how to play.

Once all options have been selected, the player can press "ENTER" to start the game.

Each turn, the player enteres the row, then the column for their cell selection. If the player thinks that cell has a mine in it, they press "f" to flag it.
If they think that cell is a number that they need to reveal, they press "ENTER".

If they flag the cell, then the cell will show an "F". The player can put in the same coordinates and press "f" again to unflag that cell if they change their mind.

If they choose to reveal the cell, and they are correct, the number of that cell will be revealed.

The number of the cell shows how many mines surround that cell.
For example, if a cell has the number 1, that means that in one of the 8 cells that surround it, there is one mine.

If the player is able to flag all of the mines on the board, and reveal all of the other cells, they win.

If at any point, the player reveals a mine, it's game over!

## Features

### Existing Features

* Customizable Board Size
  * Player can set the size of the board
  * ![Customizable Board Size](media/feature-board-size.png)
* Customizable Mine Count
  * Player can choose how many mines are in play
  * ![Customizable Mine Count](media/feature-mine-count.png)
* Instructions Page
  * Player can choose to show the instructions for the game
  * ![Instructions Page](media/feature-instructions-page.png)
* Randomly Located Bombs
  * Bombs are placed randomly on the board
* Colorization
  * The terminal is colored to add some style
* Input Validation/Error Alerts
  * Player input is validated
    * Only appropriate input is accepted
  * Incorrect inputs are alerted to the player
    * Player is alerted to incorrect input
    * Player is alerted to impossible moves
    * Plyer is alerted to already completed moves
  * ![Error Alerts](media/feature-error-alerts.png)
* Terminal Clearing
  * Terminal is cleared before each screen update
  * Keeps the information displayed relevant, and easy to read
* ASCII Drawn Board
  * To make getting the row and column easy
  * ![ASCII Drawn Board](media/feature-ascii-drawn-board.png)
* Game Results
  * Winner Screen
  * Game Over Screen
  * ![Game Results Screen - Winner](media/feature-game-results-winner.png)
  * ![Game Results Screen - Game Over](media/feature-game-results-game-over.png)

### Future Features

* Game Over Animation
  * Possible animation that plays when the game ends, transitioning to the game over screen
* Random Settings Option
  * Give the player the option to play a game with random settings
* Color Options
  * Give the player the option to change the colors used

## Data Model

## Library's/Modules

## Testing

## Deployment

## Credits
import os
import random as rand
from typing import Callable, List, Tuple


GUESSES_COUNT = 5
BOARD_SIZE_X = 5
BOARD_SIZE_Y = 5

# Constants used to represent elements on the board
HIDDEN = "0"
SHIP = "S"
GUESS = "X"


def read_int(prompt: str, min_value: int = 1, max_value: int = 5) -> int:
    """
    Read an integer between a min and max value
    """
    while True:
        line = input(prompt)
        try:
            value = int(line)
            if value not in range(min_value, max_value + 1):
                print(f"Value must be in [{min_value}, {max_value}]. Try again.")

            return value

        except ValueError:
            print("That's not a number! Try again.")


def read_guess(already_guessed: Callable[[int, int], bool]) -> Tuple[int, int]:
    while True:
        # read row and column
        guess_row = read_int("Guess row: ", max_value=5) - 1
        guess_col = read_int("Guess column: ", max_value=5) - 1

        # if the guess is valid, return the guessed row and column
        if not already_guessed(guess_row, guess_col):
            return guess_row, guess_col

        print("You've already guessed on that row! Try again.")


class BattleshipBoard:
    def __init__(self, size_x: int, size_y: int) -> None:
        # create the board
        self.grid = [[HIDDEN] * size_x for _ in range(size_y)]

        # place a random ship on the grid
        ship_row = rand.randint(0, size_x - 1)
        ship_col = rand.randint(0, size_y - 1)
        self.grid[ship_row][ship_col] = SHIP

    def is_ship(self, row: int, col: int) -> bool:
        return self.grid[row][col] == SHIP

    def already_guessed(self, row: int, col: int) -> bool:
        return self.grid[row][col] == GUESS

    def place_guess(self, row: int, col: int) -> None:
        if not self.is_ship(row, col):
            self.grid[row][col] = GUESS

    def to_string(self, show_ship: bool = False) -> str:
        rows_str: List[str] = []
        for row in self.grid:
            row_repr = [HIDDEN if col == SHIP and not show_ship else col for col in row]
            rows_str.append(" ".join(row_repr))

        return "\n".join(rows_str)


def turn(board: BattleshipBoard) -> bool:
    """
    Handle a single player's turn.
    """

    print(board.to_string())

    # let the player guess
    guess_row, guess_col = read_guess(board.already_guessed)
    board.place_guess(guess_row, guess_col)

    return board.is_ship(guess_row, guess_col)


def play_game(player_count: int, board: BattleshipBoard) -> None:
    """
    Play a game of Battleship with a given number of players.
    """
    os.system("clear")

    total_guesses = 0

    while total_guesses < GUESSES_COUNT * player_count:
        # determine the current player and the remaining guesses for that player
        current_player = (total_guesses % player_count) + 1
        remaining_guesses = GUESSES_COUNT - total_guesses // player_count

        print(f"Player {current_player}'s turn: {remaining_guesses} guesses left.")

        if turn(board):
            print(f"Congrats! Player {current_player} sank the ship!")
            break
        else:
            print("Sorry, you missed!")

        total_guesses += 1

    if total_guesses >= GUESSES_COUNT * player_count:
        print("Game over, you didn't find the ship in time.")
    print(board.to_string(show_ship=True))


def main() -> None:
    os.system("cls")
    player_count = read_int(
        "Please enter how many players are going to play: ", max_value=2
    )
    board = BattleshipBoard(BOARD_SIZE_X, BOARD_SIZE_Y)
    play_game(player_count, board)


if __name__ == "__main__":
    main()

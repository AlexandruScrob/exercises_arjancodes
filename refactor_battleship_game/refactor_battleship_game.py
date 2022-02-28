import copy as c
import os
import random as rand
from typing import Callable, Tuple


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


class Game(object):
    def __init__(self, players):
        self.guesses = 5
        self.player_list = []
        for player in range(players):
            self.player_list.append(self.guesses)
        self.current_player = 1
        self.board = self.create_matrix(5, 5)
        self.board_visible = c.deepcopy(self.board)
        self.ship_row = rand.randint(0, 4)
        self.ship_col = rand.randint(0, 4)

    """
    Defining the many methods that makes the game work,
    starting with the create_matrix where we take in the 
    boards max x and max y to define its size.
    """

    def create_matrix(self, max_x, max_y):
        matrix = list(range(max_x))
        for x in matrix:
            matrix[x] = list(range(max_y))
            for y in range(max_y):
                matrix[x][y] = "O"
        return c.deepcopy(matrix)

    """
    Defining the print_board function, here I respresent
    x as rows
    y as colums
    """

    def print_board(self, board_in):
        x = 0
        y = 0
        for column in board_in:
            y = 0
            for row in column:
                if y == 0:
                    print(" ", row, end=" ")
                elif y == len(board_in[x]):
                    print("", row, end="")
                else:
                    print(row, end=" ")
                y += 1
            print()
            x += 1
        return None

    """
    Seperating out the game_logic to try to make the main function as readable as possible.
    This is also an exercise to practice writing recursive code instead of using while loops.
    """

    def already_guessed(self, row: int, col: int) -> bool:
        return self.board[row][col] == "X"

    def game_logic(self):
        guess_row, guess_col = read_guess(self.already_guessed)

        # I first did -1 here and spread out in the code. Very bad and confusing.
        if self.board[guess_row][guess_col] == self.board[self.ship_row][self.ship_col]:
            # if self.guess_row == self.ship_row and self.guess_col == self.ship_col:
            return True
        else:
            if self.player_list[self.current_player - 1] > 0:
                print("Sorry, you missed!")
                self.board[guess_row][guess_col] = "X"
                self.board_visible[guess_row][guess_col] = "X"
                self.player_list[self.current_player - 1] -= 1
                self.print_board(self.board_visible)

                if len(self.player_list) > 1:
                    self.current_player += 1
                if self.current_player > len(self.player_list):
                    self.current_player = 1
                return self.game_logic()
            else:
                print("Player {} ran out of guesses!".format(self.current_player))
                return False

    """
    Keeping the main function simple and easy to read by handling game logic
    above and using return to see the condition of the game.
    """

    def main(self):
        os.system("clear")
        self.print_board(self.board)
        self.board[self.ship_row][self.ship_col] = "S"
        if self.game_logic() == True:
            self.board[self.ship_row][self.ship_col] = "S"
            self.print_board(self.board)
            print(
                "Congratulations! Player {} sank the ship!".format(self.current_player)
            )
        else:
            print("Game over! Player {} has lost!".format(self.current_player))
            self.print_board(self.board)


def main() -> None:
    os.system("clear")
    player_count = read_int(
        "Please enter how many players are going to play: ", max_value=2
    )
    battleship = Game(player_count)
    battleship.main()


if __name__ == "__main__":
    main()

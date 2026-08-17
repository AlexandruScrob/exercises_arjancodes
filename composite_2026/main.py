import os

from engine import Game
from level import build_level


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def main() -> None:
    game = Game(root=build_level())

    while game.running:
        clear_screen()
        print(game.render())
        print(f"Score: {game.score}")

        command = input("Command: ")[:1]

        if command == "t":
            print()
            print(game.tree())
            input("\nPress Enter to continue...")
            continue

        game.update(command)


if __name__ == "__main__":
    main()

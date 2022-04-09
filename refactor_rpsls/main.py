from game import Game
from cli import CLI


def main() -> None:

    cli = CLI()
    player_name = cli.read_player_name()
    game = Game(cli, player_name)
    game.play()


if __name__ == "__main__":
    main()

from game import Game
from cli import CLI
from scoreboard import Scoreboard


def main() -> None:

    cli = CLI()
    player_name = cli.read_player_name()
    game = Game(Scoreboard(), cli, player_name)
    game.play()


if __name__ == "__main__":
    main()

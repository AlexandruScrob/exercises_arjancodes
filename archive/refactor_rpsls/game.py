from dataclasses import dataclass
from rules import get_winner
from ui import UI
from scoreboard import Scoreboard


@dataclass
class Game:
    scoreboard: Scoreboard
    ui: UI
    player_name: str
    cpu_name: str = "cpu"

    def do_turn(self) -> None:
        player_entity = self.ui.pick_player_entity()
        cpu_entity = self.ui.pick_cpu_entity()

        self.ui.display_current_round(
            self.player_name, self.cpu_name, player_entity, cpu_entity
        )

        winner, message = get_winner(player_entity, cpu_entity)

        if not winner:
            self.ui.display_tie()
        elif winner == player_entity:
            self.ui.display_round_winner(self.player_name, player_entity, message)
            self.scoreboard.win_round(self.player_name)
        else:
            self.ui.display_round_winner(self.cpu_name, cpu_entity, message)
            self.scoreboard.win_round(self.cpu_name)

    def play(self, max_rounds: int = 5):
        # register players in scoreboard
        self.scoreboard.register_player(self.player_name)
        self.scoreboard.register_player(self.cpu_name)

        # displaying the rules of the game
        self.ui.display_rules()
        for _ in range(max_rounds):
            self.do_turn()
            self.scoreboard.to_display(self.ui)

from ui import UI
from scoreboard import Scoreboard
from rules import Rules


class Game:
    """Game class"""

    def __init__(self, ui: UI, user: str, max_round: int = 5) -> None:
        self.ui = ui
        self.scoreboard = Scoreboard()
        self.max_round = max_round
        self.rules = Rules()
        self.user: str = user
        self.cpu: str = "cpu"

        # register players in scoreboard
        self.scoreboard.register_player(self.user)
        self.scoreboard.register_player(self.cpu)

    def do_turn(self) -> None:
        """Function to continue the rounds"""
        user_entity = self.ui.pick_player_entity()
        cpu_entity = self.ui.pick_cpu_entity()

        self.ui.display_current_round(self.user, self.cpu, user_entity, cpu_entity)
        if cpu_entity == user_entity:
            self.ui.display_tie()
            return

        winner, message = self.rules.get_winner(user_entity, cpu_entity)
        if winner == user_entity:
            self.ui.display_round_winner(self.user, user_entity, message)
            self.scoreboard.points[self.user] += 1
        else:
            self.ui.display_round_winner(self.cpu, cpu_entity, message)
            self.scoreboard.points[self.cpu] += 1

    def play(self):
        self.ui.display_rules()
        for _ in range(self.max_round):
            self.do_turn()
            self.scoreboard.display_scores()

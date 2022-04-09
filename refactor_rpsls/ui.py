from typing import Protocol
from entity import Entity


class UI(Protocol):
    def pick_player_entity(self) -> Entity:
        raise NotImplementedError()

    def pick_cpu_entity(self) -> Entity:
        raise NotImplementedError()

    def read_player_name(self) -> str:
        raise NotImplementedError()

    def display_rules(self) -> None:
        raise NotImplementedError()

    def display_current_round(
        self, player_name: str, cpu_name: str, player_entity: Entity, cpu_entity: Entity
    ) -> None:
        raise NotImplementedError()

    def display_tie(self) -> None:
        raise NotImplementedError()

    def display_round_winner(
        self, winner_name: str, winner_entity: Entity, message: str
    ) -> None:
        raise NotImplementedError()

    def display_scores(self, scores: dict[str, int]) -> None:
        raise NotImplementedError()

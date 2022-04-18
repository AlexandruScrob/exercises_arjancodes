from enum import Enum


class Entity(Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSOR = "scissor"
    SPOCK = "spock"
    LIZARD = "lizzard"

    def __str__(self) -> str:
        return self.value

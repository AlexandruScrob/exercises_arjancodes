from typing import Protocol
import time


class Game(Protocol):
    
    def update(self) -> None:
        ...
    
    @property
    def raw_grid(self) -> list[list[int]]:
        ...
    


def visualize_console(game: Game, generations: int, sleep_time: float) -> None:
    for generation in range(1, generations + 1):
        game.update()
        print(f"Generation {generation}:\n")
        print(game.grid)
        time.sleep(sleep_time)

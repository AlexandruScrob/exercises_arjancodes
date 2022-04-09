import random
from entity import Entity


def _entities_str() -> str:
    """Displays the user choices"""
    return ", ".join(f"({entity.value} for {entity.name})" for entity in Entity)


class CLI:
    def pick_player_entity(self) -> Entity:
        available_choices = [entity.value for entity in Entity]
        while True:
            try:
                print(f"Select {_entities_str()}:", end="\t")
                choice = int(input())

                if choice not in available_choices:
                    print("Please select from available choices")
                else:
                    return Entity(choice)
            except ValueError:
                print("You entered something other than a number")

    def pick_cpu_entity(self) -> Entity:
        cpu_choice = random.randint(1, len(Entity))
        return Entity(cpu_choice)

    def read_player_name(self) -> str:
        print("Please enter your name:", end="\t")
        return input().strip()

    def display_rules(self) -> None:
        print("Rock paper scissor spock and lizard...\n Welcome to the game.")
        print("Rules are simple...")
        print(
            "Scissors decapitate Lizard, Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors."
        )
        print("To begin press [Enter]")
        _ = input()

    def display_current_round(
        self, player_name: str, cpu_name: str, player_entity: Entity, cpu_entity: Entity
    ) -> None:
        print(f"{player_name} ({player_entity.name}) x {cpu_name} ({cpu_entity.name})")
        print("....")

    def display_tie(self) -> None:
        print("It's a tie..")

    def display_round_winner(
        self, winner_name: str, winner_entity: Entity, message: str
    ) -> None:
        print(f"{winner_name} ({winner_entity.name}) wins the round as {message}")

    def display_scores(self, scores: dict[str, int]) -> None:
        raise NotImplementedError()

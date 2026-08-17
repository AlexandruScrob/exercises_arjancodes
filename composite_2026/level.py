from engine import CompositeGameObject
from objects import Bunker, InvaderFleet, Player, ScoreHud


def build_level() -> CompositeGameObject:
    return CompositeGameObject(
        "Level",
        [
            CompositeGameObject(
                "World",
                [
                    InvaderFleet(),
                    CompositeGameObject("Bullets"),
                    Player(x=20, y=15),
                ],
            ),
            CompositeGameObject(
                "Bunkers",
                [
                    Bunker(6, 12),
                    Bunker(17, 12),
                    Bunker(28, 12),
                ],
            ),
            ScoreHud(),
        ],
    )

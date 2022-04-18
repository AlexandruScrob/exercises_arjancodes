from entity import Entity
from typing import Dict, Optional, Tuple


RULES: Dict[Tuple[Entity, Entity], str] = {
    (Entity.PAPER, Entity.ROCK): "covers",
    (Entity.PAPER, Entity.SPOCK): "disproves",
    (Entity.ROCK, Entity.LIZARD): "crushes",
    (Entity.ROCK, Entity.SCISSOR): "crushes",
    (Entity.SCISSOR, Entity.PAPER): "cuts",
    (Entity.SCISSOR, Entity.LIZARD): "decapitates",
    (Entity.SPOCK, Entity.SCISSOR): "smashes",
    (Entity.SPOCK, Entity.ROCK): "vaporizes",
    (Entity.LIZARD, Entity.SPOCK): "poisons",
    (Entity.LIZARD, Entity.PAPER): "eats",
}


def get_winner(entity1: Entity, entity2: Entity) -> Tuple[Optional[Entity], str]:
    if entity1 == entity2:
        return None, "It's a tie"
    if (entity1, entity2) in RULES:
        return (entity1, f"{entity1.name} {RULES[(entity1, entity2)]} {entity2.name}")
    elif (entity2, entity1) in RULES:
        return (entity2, f"{entity2.name} {RULES[(entity2, entity1)]} {entity1.name}")
    raise KeyError("Invalid entities")

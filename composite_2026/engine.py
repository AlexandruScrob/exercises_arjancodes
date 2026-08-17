from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol


class Canvas:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.pixels = [[" " for _ in range(width)] for _ in range(height)]

    def draw(self, x: int, y: int, char: str) -> None:
        if 0 <= x < self.width and 0 <= y < self.height:
            self.pixels[y][x] = char

    def draw_text(self, x: int, y: int, text: str) -> None:
        for offset, char in enumerate(text):
            self.draw(x + offset, y, char)

    def to_text(self) -> str:
        border = "+" + "-" * self.width + "+"
        rows = ["|" + "".join(row) + "|" for row in self.pixels]
        return "\n".join([border, *rows, border])


class GameObject(Protocol):
    name: str
    alive: bool

    def update(self, game: Game) -> None: ...

    def render(self, canvas: Canvas) -> None: ...

    def tree(self, indent: int = 0) -> str: ...


@dataclass
class CompositeGameObject:
    name: str
    children: list[GameObject] = field(default_factory=list[GameObject])
    alive: bool = True

    def add(self, child: GameObject) -> None:
        self.children.append(child)

    def update(self, game: Game) -> None:
        self.on_update(game)

        for child in self.children:
            child.update(game)

        self.children = [child for child in self.children if child.alive]

    def render(self, canvas: Canvas) -> None:
        self.on_render(canvas)

        for child in self.children:
            child.render(canvas)

    def tree(self, indent: int = 0) -> str:
        lines = [" " * indent + f"+ {self.name}"]

        for child in self.children:
            lines.append(child.tree(indent + 2))

        return "\n".join(lines)

    def on_update(self, game: Game) -> None:
        pass

    def on_render(self, canvas: Canvas) -> None:
        pass


@dataclass
class Game:
    root: GameObject
    width: int = 40
    height: int = 18
    command: str = ""
    tick: int = 0
    score: int = 0
    running: bool = True

    def update(self, command: str) -> None:
        self.command = command

        if command == "q":
            self.running = False
            return

        self.root.update(self)
        self.tick += 1

    def render(self) -> str:
        canvas = Canvas(self.width, self.height)
        self.root.render(canvas)
        return canvas.to_text()

    def tree(self) -> str:
        return self.root.tree()


def find_all[T](
    root: GameObject,
    cls: type[T],
) -> list[T]:
    matches: list[T] = []

    if isinstance(root, cls):
        matches.append(root)

    if isinstance(root, CompositeGameObject):
        for child in root.children:
            matches.extend(find_all(child, cls))

    return matches


def find_group(root: GameObject, name: str) -> CompositeGameObject:
    if isinstance(root, CompositeGameObject) and root.name == name:
        return root

    if isinstance(root, CompositeGameObject):
        for child in root.children:
            try:
                return find_group(child, name)
            except LookupError:
                pass

    raise LookupError(f"Group not found: {name}")

from dataclasses import dataclass

from engine import Canvas, CompositeGameObject, Game, find_all, find_group


@dataclass
class Sprite:
    name: str
    x: int
    y: int
    char: str
    alive: bool = True

    def update(self, game: Game) -> None:
        self.on_update(game)

    def render(self, canvas: Canvas) -> None:
        canvas.draw(self.x, self.y, self.char)

    def on_update(self, game: Game) -> None:
        pass

    def tree(self, indent: int = 0) -> str:
        return " " * indent + f"- {self.name}"


class Player(Sprite):
    def __init__(self, x: int, y: int) -> None:
        super().__init__("Player", x, y, "A")

    def on_update(self, game: Game) -> None:
        if game.command == "a":
            self.x = max(0, self.x - 1)

        if game.command == "d":
            self.x = min(game.width - 1, self.x + 1)

        if game.command == " ":
            bullets = find_group(game.root, "Bullets")
            bullets.add(Bullet(self.x, self.y - 1))


class Bullet(Sprite):
    def __init__(self, x: int, y: int) -> None:
        super().__init__("Bullet", x, y, "|")

    def on_update(self, game: Game) -> None:
        self.y -= 1

        if self.y < 0:
            self.alive = False


class Invader(Sprite):
    def __init__(self, x: int, y: int) -> None:
        super().__init__("Invader", x, y, "W")

    def on_update(self, game: Game) -> None:
        for bullet in find_all(game.root, Bullet):
            if bullet.alive and bullet.x == self.x and bullet.y == self.y:
                bullet.alive = False
                self.alive = False
                game.score += 10


class Bunker(Sprite):
    def __init__(self, x: int, y: int) -> None:
        super().__init__("Bunker", x, y, "#")

    def render(self, canvas: Canvas) -> None:
        for offset in range(5):
            canvas.draw(self.x + offset, self.y, "#")


class InvaderFleet(CompositeGameObject):
    def __init__(self) -> None:
        super().__init__("InvaderFleet")
        self.direction = 1

        for row in range(3):
            invader_row = CompositeGameObject(f"InvaderRow {row + 1}")

            for col in range(8):
                invader_row.add(Invader(x=4 + col * 4, y=2 + row * 2))

            self.add(invader_row)

    def on_update(self, game: Game) -> None:
        invaders = list(find_all(game.root, Invader))

        if not invaders:
            return

        if game.tick % 2 != 0:
            return

        should_turn = any(
            invader.x + self.direction < 0 or invader.x + self.direction >= game.width
            for invader in invaders
        )

        if should_turn:
            self.direction *= -1

            for invader in invaders:
                invader.y += 1
        else:
            for invader in invaders:
                invader.x += self.direction


class ScoreHud(CompositeGameObject):
    def __init__(self) -> None:
        super().__init__("HUD")

    def on_render(self, canvas: Canvas) -> None:
        canvas.draw_text(
            1,
            canvas.height - 1,
            "a/d move | space fire | t tree | q quit",
        )

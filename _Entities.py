# -------------------------------------------------
# Entity definition
# -------------------------------------------------
class Entity:
    def __init__(self, name: str, sprite, position) -> None:
        self.name = name
        self.sprite = sprite
        self.position = position


class Fighter(Entity):
    def __init__(
        self,
        health: int,
        name: str,
        sprite,
        position,
    ):
        self.health = health
        super().__init__(name, sprite, position)

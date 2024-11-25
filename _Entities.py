# -------------------------------------------------
# Entity definition
# -------------------------------------------------
class Entity:
    def __init__(self, name: str, sprite, position, collider=None) -> None:
        self.name = name
        self.sprite = sprite
        self.position = position
        self.collider = collider


class Fighter(Entity):
    def __init__(
        self,
        health: int,
        name: str,
        sprite,
        position,
        collider=None,
    ):
        self.health = health
        super().__init__(name, sprite, position, collider)

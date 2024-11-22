from _Engine import *

player = Fighter(10, "Bob", Sprite(Pixel(Vector(0, 0), "B")), Vector(0, 0))

def check_player_position() -> Vector:
    """
    >>> check_player_position()
    (0, 0)
    """
    return player.position.x, player.position.y
### Summary :
###     Definition of classes that contain data for rendering with in-game screen
###     These don't depend on game logic

import _Types as Types


class Pixel:
    def __init__(self, character="+", position=Types.Vector(0, 0)):
        self.position = position
        self.character = character


class Sprite:
    def __init__(self, pixels: Types.Array, z_index=0, offset = Types.Vector(0, 0)):
        self.pixels = pixels
        self.z_index = z_index
        self.offset = offset


class Sprite_Library:
    default_square = Sprite(
        [
            Pixel("_", Types.Vector(1, 0)),
            Pixel("_", Types.Vector(2, 0)),
            Pixel("_", Types.Vector(3, 0)),
            Pixel("_", Types.Vector(4, 0)),
            Pixel("_", Types.Vector(0, 0)),
            Pixel("_", Types.Vector(5, 0)),
            Pixel("|", Types.Vector(0, 1)),
            Pixel("|", Types.Vector(0, 2)),
            Pixel("|", Types.Vector(0, 3)),
            Pixel("|", Types.Vector(0, 4)),
            Pixel("|", Types.Vector(0, 5)),
            Pixel("|", Types.Vector(5, 1)),
            Pixel("|", Types.Vector(5, 2)),
            Pixel("|", Types.Vector(5, 3)),
            Pixel("|", Types.Vector(5, 4)),
            Pixel("|", Types.Vector(5, 5)),
            Pixel("_", Types.Vector(1, 5)),
            Pixel("_", Types.Vector(2, 5)),
            Pixel("_", Types.Vector(3, 5)),
            Pixel("_", Types.Vector(4, 5)),
        ]
    )
    light_effect = Sprite(
        [
            Pixel(".", Types.Vector(1, 0)),
            Pixel(".", Types.Vector(2, 0)),
            Pixel(".", Types.Vector(3, 0)),
            Pixel(".", Types.Vector(4, 1)),
            Pixel(".", Types.Vector(4, 2)),
            Pixel(".", Types.Vector(4, 3)),
            Pixel(".", Types.Vector(3, 1)),
            Pixel(".", Types.Vector(3, 2)),
            Pixel(".", Types.Vector(3, 3)),
            Pixel(".", Types.Vector(2, 1)),
            Pixel(".", Types.Vector(2, 2)),
            Pixel(".", Types.Vector(2, 3)),
            Pixel(".", Types.Vector(1, 1)),
            Pixel(".", Types.Vector(1, 2)),
            Pixel(".", Types.Vector(1, 3)),
            Pixel(".", Types.Vector(0, 1)),
            Pixel(".", Types.Vector(0, 2)),
            Pixel(".", Types.Vector(0, 3)),
            Pixel(".", Types.Vector(1, 4)),
            Pixel(".", Types.Vector(2, 4)),
            Pixel(".", Types.Vector(3, 4)),
        ],
        -100,
        Types.Vector(-2, -2)
    )

    player_sprite = Sprite([Pixel("P")], 10)

    goblin_sprite = Sprite([Pixel("G")], 5)

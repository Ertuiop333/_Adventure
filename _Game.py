from _Engine import *

SCREEN_WIDTH = 20
SCREEN_HEIGHT = 20

stop_game_event = False

player = Fighter(
    10,
    "Bob",
    Sprite_Library.player_sprite,
    Vector(2, 2)
    )

box = Entity(
    "box",
    Sprite_Library.default_square,
    Vector(0, 10)
    )

def game_loop():
    reset_screen(".", "  ", SCREEN_WIDTH, SCREEN_HEIGHT)
    add_drawable_entity(box)
    add_drawable_entity(player)
    update_screen()

    last_input = None

    while True:
        i = input("move : ").lower()
        if i == "":
            i = last_input
        last_input = i

        if i == "a":
            player.position.x -= 1
        elif i == "d":
            player.position.x += 1
        elif i == "w":
            player.position.y -= 1
        elif i == "s":
            player.position.y += 1
        
        update_screen()


if __name__ == "__main__":
    game_loop()


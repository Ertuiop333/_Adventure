### Summary :
###     Definition of main game loop.
###     Depends on pretty much everything in the program.
###     Should never be imported.

import _Types as Types
import _Entities as Entities

import s_Terminal as Terminal
import s_Visuals as Visuals
import s_Collisions as Collisions

import u_Logic as Logic
import u_Rendering as Rendering
import u_Physics as Physics

SCREEN_WIDTH = 20
SCREEN_HEIGHT = 20

stop_game_event = False

player = Entities.Fighter(
    10,
    "Bob",
    Visuals.Sprite_Library.player_sprite,
    Types.Vector(2, 2),
    Collisions.ColliderLibrary.single_point,
)

box = Entities.Entity(
    "box",
    Visuals.Sprite_Library.default_square,
    Types.Vector(0, 0),
    Collisions.empty_box(5, 5),
)

enemy = Entities.Fighter(
    5,
    "Goblin",
    Visuals.Sprite_Library.goblin_sprite,
    Types.Vector(5, 5),
    Collisions.ColliderLibrary.single_point,
)


def start():
    Terminal.reset_in_game_screen(".", " ", 10, 10)

    Rendering.add_object_to_render_queue(
        Rendering.RenderObject(box.sprite, box.position)
    )
    Rendering.add_object_to_render_queue(
        Rendering.RenderObject(player.sprite, player.position)
    )
    Rendering.add_object_to_render_queue(
        Rendering.RenderObject(enemy.sprite, enemy.position)
    )


def game_loop():
    global stop_game_event

    last_input = None

    while stop_game_event == False:
        # DRAW
        Terminal.__reset_screen_buffer()
        Rendering.write_render_queue_to_screen_data()
        Terminal.update_in_game_screen()

        # INPUT
        i = input("MOVE: ").lower()

        # UPDATE
        if i == "":
            i = last_input
        else:
            last_input = i

        if i == "a":
            player.position.x -= 1
        elif i == "d":
            if (
                Physics.is_object_colliding_with_other_object(
                    Physics.PhysicsObject(
                        player.collider, player.position + Types.Vector(1, 0)
                    ),
                    Physics.PhysicsObject(box.collider, box.position),
                )
                == False
            ):
                player.position.x += 1
        elif i == "w":
            player.position.y -= 1
        elif i == "s":
            player.position.y += 1
        elif i == "quit":
            stop_game_event = True
        elif len(i) > 30:
            stop_game_event = True


if __name__ == "__main__":
    start()
    game_loop()

### Summary :
###     Definition of main game loop.
###     Depends on pretty much everything in the program.
###     Should never be imported.

import _Types as Types
import _Entities as Entities

import s_Terminal as Terminal
import s_Visuals as Visuals
import s_Collisions as Collisions

import u_Rendering as Rendering
import u_Physics as Physics

import h_Logic as Logic


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
    Collisions.empty_box(6, 6),
)

enemy = Entities.Fighter(
    5,
    "Goblin",
    Visuals.Sprite_Library.goblin_sprite,
    Types.Vector(5, 5),
    Collisions.ColliderLibrary.single_point,
)

move_action_list = Types.Array().new_1d_empty()
move_prompt_message = "DIRECTION:\n    (w)    \n(a) (s) (d)\n->"


def start():
    global move_action_list
    move_action_list = [
        ["up   (w)", "w"],
        ["down (s)", "s"],
        ["left (a)", "a"],
        ["right(d)", "d"],
    ]

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

    Physics.add_object_to_physics(
        Physics.PhysicsObject(player.collider, player.position, "player")
    )
    Physics.add_object_to_physics(Physics.PhysicsObject(box.collider, box.position))


def game_loop():
    global stop_game_event

    last_input = None

    while stop_game_event == False:
        # DRAW
        Terminal.__reset_screen_buffer()
        Rendering.write_render_queue_to_screen_data()
        Terminal.update_in_game_screen()

        # INPUT
        i = Terminal.create_choice_prompt(move_action_list, False, move_prompt_message)

        # UPDATE
        if i == "":
            i = last_input
        else:
            last_input = i

        move = Types.Vector(0, 0)
        if i == "a":
            move = Types.Vector(-1, 0)
        elif i == "d":
            player.position.x += 1
        elif i == "w":
            move = Types.Vector(0, -1)
        elif i == "s":
            move = Types.Vector(0, 1)
        elif i == "quit":
            stop_game_event = True

        Rendering.add_object_to_render_queue(
            Rendering.RenderObject(player.sprite, player.position)
        )

        # player.position = Logic.try_move_entity(player, move)


if __name__ == "__main__":
    start()
    game_loop()

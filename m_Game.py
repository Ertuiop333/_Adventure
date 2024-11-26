### Summary :
###     Definition of main game loop.
###     Depends on pretty much everything in the program.
###     Should never be imported.

import _Types as Types

import s_Terminal as Terminal

import u_Rendering as Rendering

import h_Logic as Logic
import h_Initialization as Initialization


SCREEN_WIDTH = 20
SCREEN_HEIGHT = 20

stop_game_event = False

init_data: Initialization.InitData

move_action_list = Types.Array().new_1d_empty()
move_prompt_message = "DIRECTION:\n    (w)    \n(a) (s) (d)\n->"


def start():
    global init_data
    init_data = Initialization.initialize()

    global move_action_list
    move_action_list = [
        ["up   (w)", "w"],
        ["down (s)", "s"],
        ["left (a)", "a"],
        ["right(d)", "d"],
    ]

    Terminal.reset_in_game_screen(".", " ", 10, 10)


last_input = "quit"


def program_commands(i: str):
    global last_input
    global stop_game_event
    if i == "quit":
        stop_game_event = True
    elif i == "":
        i = last_input
    else:
        last_input = i


def game_loop():
    global stop_game_event

    player = init_data.player
    box = init_data.box

    while stop_game_event == False:
        # DRAW
        Terminal.__reset_screen_buffer()
        Rendering.write_render_queue_to_screen_data()
        Terminal.update_in_game_screen()

        # INPUT
        i = Terminal.create_choice_prompt(move_action_list, False, move_prompt_message)

        # UPDATE
        move = Logic.handle_move_inputs(i)
        Logic.move_entity(player, move, box)

        program_commands(i)


if __name__ == "__main__":
    start()
    game_loop()

### Summary :
###     Definition of main game loop.
###     Depends on pretty much everything in the program.
###     Should never be imported.

import _Types as Types

import s_Terminal as Terminal

import u_Rendering as Rendering

import h_Logic as Logic
import h_Initialization as Initialization


SCREEN_WIDTH = 10
SCREEN_HEIGHT = 10

stop_game_event = False

init_data: Initialization.InitData

camera_pos = Types.Vector(0, 0)
camera_focus_area = Types.Area(Types.Vector(2, 2), Types.Vector(7, 7))

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

    Terminal.reset_in_game_screen(".", " ", SCREEN_WIDTH, SCREEN_HEIGHT)


last_input = "quit"
i = ""


def program_commands():
    global last_input
    global i
    global stop_game_event
    
    if i == "quit":
        stop_game_event = True
    if i == "":
        i = last_input

    last_input = i    


def game_loop():
    global stop_game_event
    global i

    player = init_data.player
    box = init_data.box

    while stop_game_event == False:
        # DRAW
        Terminal.__reset_screen_buffer()
        Rendering.write_render_queue_to_screen_data(camera_pos)
        Terminal.update_in_game_screen()

        # INPUT
        i = Terminal.create_choice_prompt(move_action_list, False, move_prompt_message)

        # UPDATE
        program_commands()

        move = Logic.handle_move_inputs(i)
        Logic.move_entity(player, move, box)

        if player.position.x > camera_pos.x + camera_focus_area.extent.x:
            camera_pos.x += 1
        if player.position.x < camera_pos.x + camera_focus_area.origin.x:
            camera_pos.x -= 1
        if player.position.y > camera_pos.y + camera_focus_area.extent.y:
            camera_pos.y += 1
        if player.position.y < camera_pos.y + camera_focus_area.origin.y:
            camera_pos.y -= 1



if __name__ == "__main__":
    start()
    game_loop()

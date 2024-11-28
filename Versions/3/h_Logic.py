### Summary :
###     Definition of variable types that are specific to the game
###     These depend on all game logic

import _Types as Types

import s_Entities as Entities
import s_Terminal as Terminal

import u_Components as Components
import u_Rendering as Rendering
import u_Physics as Physics

import h_Objects as Objects


camera_pos = Types.Vector(0, 0)
camera_focus_area = Types.Area(Types.Vector(2, 2), Types.Vector(11, 7))

# -------------------------------------------------
# Entities
# -------------------------------------------------
player: Entities.Entity
box: Entities.Entity

def update_camera_pos_based_on_player_pos(player_pos: Types.Vector, camera_pos: Types.Vector, camera_focus_area: Types.Area) -> Types.Vector:
    if player_pos.x > camera_pos.x + camera_focus_area.extent.x:
        camera_pos.x += 1
    if player_pos.x < camera_pos.x + camera_focus_area.origin.x:
        camera_pos.x -= 1
    if player_pos.y > camera_pos.y + camera_focus_area.extent.y:
        camera_pos.y += 1
    if player_pos.y < camera_pos.y + camera_focus_area.origin.y:
        camera_pos.y -= 1


def move_entity(entity: Entities.Entity, movement: Types.Vector):
    entity.position += movement
    physic_component = entity.try_get_component_of_type(Components.Physic)
    if physic_component != None:
        if (
            Physics.is_object_colliding_with_any_other_registered_object(
                physic_component
            )
            == True
        ):
            entity.position -= movement
    
    global camera_pos
    global camera_focus_area
    global player
    update_camera_pos_based_on_player_pos(player.position, camera_pos, camera_focus_area)

def handle_move_inputs(i: str) -> Types.Vector:
    move = Types.Vector(0, 0)

    if i == "a":
        move = Types.Vector(-1, 0)
    elif i == "d":
        move = Types.Vector(1, 0)
    elif i == "w":
        move = Types.Vector(0, -1)
    elif i == "s":
        move = Types.Vector(0, 1)

    return move

# -------------------------------------------------
# Draw
# -------------------------------------------------
def draw():
    global camera_pos

    Terminal.__reset_screen_buffer()
    Rendering.write_render_queue_to_screen_data(camera_pos)
    Terminal.update_in_game_screen()

# -------------------------------------------------
# Inputs
# -------------------------------------------------

last_input = ""
i = ""

move_prompt_message = "DIRECTION:\n    (w)    \n(a) (s) (d)\n->"
move_action_list: str

def input() -> bool:
    global i

    i = Terminal.create_choice_prompt(move_action_list, False, move_prompt_message)

    stop_game_event = False
    stop_game_event, i = program_commands()

    return stop_game_event

def program_commands():
    global last_input
    global i
    
    stop_game_event: bool = False
    
    if i == "quit":
        stop_game_event = True
    if i == "":
        i = last_input

    last_input = i   

    return stop_game_event, i

# -------------------------------------------------
# Program
# -------------------------------------------------

def start():
    global move_action_list
    move_action_list = [
        ["up   (w)", "w"],
        ["down (s)", "s"],
        ["left (a)", "a"],
        ["right(d)", "d"],
    ]

    init_data = Objects.generate()

    global player
    global box

    player = init_data.player
    box = init_data.box

def update():
    move = handle_move_inputs(i)
    move_entity(player, move)
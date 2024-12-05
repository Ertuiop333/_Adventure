### Summary :
###     Definition of variable types that are specific to the game
###     These depend on all game logic

import _Types as Types

import s_Entities as Entities
import s_Terminal as Terminal
import s_Visuals as Visuals

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
grid: Entities.Entity

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

position_prompt_message = "1|2|3\n4|5|6\n7|8|9\n->"
positions_list: str

def _input() -> bool:
    global i

    # i = Terminal.create_choice_prompt(move_action_list, False, move_prompt_message)

    all_inputs = []
    for i in range(len(move_action_list)):
        all_inputs.append(move_action_list[i])
    for i in range(len(positions_list)):
        all_inputs.append(positions_list[i])

    i = Terminal.create_choice_prompt(all_inputs, False, position_prompt_message)

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

    global positions_list
    positions_list = [
        ["1", "1"],
        ["2", "2"],
        ["3", "3"],
        ["4", "4"],
        ["5", "5"],
        ["6", "6"],
        ["7", "7"],
        ["8", "8"],
        ["9", "9"],
    ]

    init_data = Objects.generate()

    global player
    global grid

    player = init_data.player
    grid = init_data.box

    grid.add_component(Grid(grid, [0, 0, 0, 0, 0, 0, 0, 0, 0]))

    global grid_component
    grid_component = grid.try_get_component_of_type(Grid)


class Grid(Components.Component):
    def __init__(self, master_entity, positions: list):
        super().__init__(master_entity)
        self.positions = positions
    
    def try_play_move(self, position, player) -> bool:
        if self.positions[position-1] == 0:
            self.positions[position-1] = player

            relative_x = ((position - 1) % 3)* 2
            relative_y = ((position - 1) // 3) * 2
            y = self.master_entity.position.y + relative_y
            x = self.master_entity.position.x + relative_x

            symbol = "O"
            if player == 1:
                symbol = "X"

            mark = Entities.Entity("mark", Types.Vector(x, y), [])
            mark.components = [
                Components.Renderer(mark, Visuals.Sprite([Visuals.Pixel(symbol)], 100))
            ]
            Rendering.add_object_to_render_queue(mark.try_get_component_of_type(Components.Renderer))

            return True
        return False

player_turn = 1
grid_component: Grid
def update():
    # try:
    #     move = handle_move_inputs(int(i))
    #     move_entity(player, move)
    # except:
    #     global player_turn

    #     pos = int(i)

    #     if grid_component.try_play_move(pos, player_turn):
    #         player_turn *= -1

    #     input(f"{grid_component.positions[:]}")
    pass
    

    

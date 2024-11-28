### Summary :
###     Definition of variable types that are specific to the game
###     These depend on game logic

import _Types as Types
import s_Entities as Entities

import u_Components as Components

import u_Physics as Physics


# -------------------------------------------------
# Room definition
# -------------------------------------------------
# class Room:
#     def __init__(
#         self,
#         actions=["action1", "action_2", "action 3"],
#     ) -> None:
#         self.actions = actions

#     def enter(self, player):
#         greeting = player.name + " entered a room. \n"
#         print(greeting + self.description)
#         action = Terminal.create_choice_prompt(self.actions)
#         print(action)
#         input("")
#         Terminal.clear_terminal()


# -------------------------------------------------
# Entity movements
# -------------------------------------------------


def move_entity(entity: Entities.Entity, movement: Types.Vector, box: Entities.Entity):
    entity.position += movement
    physic_component = entity.try_get_component_of_type(Components.Physic)
    if physic_component != None:
        if (
            Physics.is_object_colliding_with_other_object(
                physic_component, box.components[1]
            )
            == True
        ):
            entity.position -= movement


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

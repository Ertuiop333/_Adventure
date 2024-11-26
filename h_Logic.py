### Summary :
###     Definition of variable types that are specific to the game
###     These depend on game logic

import _Types as Types
import _Entities as Entities

import s_Terminal as Terminal

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
# Player movements
# -------------------------------------------------


# def try_move_entity(entity: Entities.Entity, move: Types.Vector) -> Types.Vector:
#     collision_at_target_position = (
#         Physics.is_object_colliding_with_any_other_registered_object(
#             Physics.PhysicsObject(entity.collider, entity.position + move)
#         )
#     )

#     if collision_at_target_position:
#         return entity.position
#     else:
#         return entity.position + move

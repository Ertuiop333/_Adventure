### Summary :
###     Definition of variable types that are specific to the game
###     These depend on game logic

import _Types as Types

import s_Terminal as Terminal


# -------------------------------------------------
# Room definition
# -------------------------------------------------
class Room:
    def __init__(
        self,
        actions=["action1", "action_2", "action 3"],
    ) -> None:
        self.actions = actions

    def enter(self, player):
        greeting = player.name + " entered a room. \n"
        print(greeting + self.description)
        action = Terminal.create_choice_prompt(self.actions)
        print(action)
        input("")
        Terminal.clear_terminal()

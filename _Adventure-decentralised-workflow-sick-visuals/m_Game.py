### Summary :
###     Definition of main game loop.
###     Depends on pretty much everything in the program.
###     Should never be imported.

import _Types as Types

import s_Terminal as Terminal

import h_Logic as Logic


SCREEN_WIDTH = 14
SCREEN_HEIGHT = 10


def start():
    Logic.start()
    Terminal.reset_in_game_screen(" ", " ", SCREEN_WIDTH, SCREEN_HEIGHT)

def game_loop():
    stop_game_event: bool = False

    while stop_game_event == False:
        # DRAW
        Logic.draw()

        # INPUT
        stop_game_event = Logic.input()

        # UPDATE
        Logic.update()


if __name__ == "__main__":
    start()
    game_loop()

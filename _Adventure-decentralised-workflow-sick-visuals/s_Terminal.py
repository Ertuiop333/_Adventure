### Summary :
###     Definition of functions that are specific to the game
###     These don't depend on game logic

from os import system, name
import _Types as Types


# -------------------------------------------------
# Terminal
# -------------------------------------------------
def clear_terminal():
    # for windows
    if name == "nt":
        _ = system("cls")

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def create_choice_prompt(
    action_list: Types.Array,
    print_action_list=True,
    prompt_message="\nQu'allez-vous faire?",
    error_message="Cette entrée est invalide. Veuillez réessayer.",
):
    input_valid = False

    while input_valid != True:
        if print_action_list:
            i = 1
            for k in action_list:
                print(str(i) + "- " + k)
                i += 1

        test_input = input(prompt_message).lower()

        # for users that enter the numbers
        try:
            if int(test_input) <= i:
                return action_list[int(test_input) - 1]
        except:
            pass

        # for users that enter the key
        for k in action_list:
            if test_input == k[1]:
                return k[1]

        if test_input == "":
            return ""

        if len(test_input) > 30 or test_input == "quit" or test_input == "q":
            return "quit"

        print(error_message)


# -------------------------------------------------
# In-game screen
# -------------------------------------------------

# we save the last settings of in-game screen reset/update/etc.
__x: int = 5
__y: int = 5
__character: str = "."
__space_between_pixels: str = " "

screen_data = Types.Array().new_2d_empty(__x, __y, ".")


def reset_in_game_screen(character=None, space=None, xSize=None, ySize=None):
    global __x
    global __y
    global __character
    global __space_between_pixels

    # use last saved settings if none were given
    if character == None:
        character = __character
    if space == None:
        space = __space_between_pixels
    if xSize == None:
        xSize = __x
    if ySize == None:
        ySize = __y

    # save the last settings of in-game screen reset/update/etc.
    __x = xSize
    __y = ySize
    __character = character
    __space_between_pixels = space

    clear_terminal()
    __reset_screen_buffer(character)
    update_in_game_screen()


def __reset_screen_buffer(character=None):
    global screen_data

    screen_data = Types.Array().new_2d_empty(__x, __y, ".")

    if character == None:
        character = __character

    for i in range(__x):
        for j in range(__y):
            screen_data[i][j] = str(character)


def update_in_game_screen():
    # use last saved settings
    global __x
    global __y
    global __space_between_pixels
    global screen_data

    clear_terminal()

    for j in range(__y):
        for i in range(__x):
            print(screen_data[i][j], end=__space_between_pixels)
        print("")

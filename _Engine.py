from os import system, name

def create_2d_array(rows, cols, default_value=None):
    return [[default_value for _ in range(cols)] for _ in range(rows)]

# -------------------------------------------------
# Terminal Screen
# -------------------------------------------------
class ActionList():
    def __init__(self, actions_names) -> None:
        self.actions_names = actions_names

def create_choice_prompt(action_list : ActionList, prompt_message = "which one? : ", error_message = "wait... that's not an action! pick one of these:"):
        input_valid = False

        while input_valid != True:
            i = 1
            for c in action_list.actions_names:
                print(str(i) + "- " + c)
                i += 1
            test_input = input(prompt_message).lower()

            #for users that enter the numbers
            try:
                if int(test_input) <= i:
                    return action_list[int(test_input) - 1]
            except:
                pass
            
            #for users that enter the text
            for c in action_list:
                if test_input == c:
                    return c
            
            print(error_message)

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear') 

__x : int = 5
__y : int = 5



def reset_screen(character = ".", space = " ", xSize = 5, ySize = 5):
    clear()
    global screen_data

    global __x 
    __x = xSize

    global __y
    __y = ySize

    global space_string_memory
    space_string_memory = space

    reset_screen_buffer(character)
    update_screen(space_string_memory)

def reset_screen_buffer(character = "."):
    global screen_data
    screen_data = create_2d_array(__x, __y, ".")

    for i in range(__x):
        for j in range(__y):
            screen_data[i][j] = str(character)


# -------------------------------------------------
# Vector definition
# -------------------------------------------------
class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    x = 0
    y = 0

    def __str__(self):
        # Custom string representation
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x + other, self.y + other)
        else:
            raise TypeError("Unsupported operand type for +")
# -------------------------------------------------
# visual assets
# -------------------------------------------------
class Pixel:
    position = Vector()
    character = "P"

    def __init__(self, character = "+", position = Vector(0, 0)):
        self.position = position
        self.character = character

class Sprite:
    def __init__(self, pixels = [Pixel(Vector(), "0") for i in range(10)], z_index = 0):
        self.pixels = pixels
        self.z_index = z_index

    pixels : list[Pixel]


class Sprite_Library:
    default_square = Sprite([
        Pixel("-", Vector(1, 0)),
        Pixel("-", Vector(2, 0)),
        Pixel("-", Vector(3, 0)),
        Pixel("-", Vector(4, 0)),

        Pixel("|", Vector(0, 0)),
        Pixel("|", Vector(5, 0)),
        Pixel("|", Vector(0, 1)),
        Pixel("|", Vector(0, 2)),
        Pixel("|", Vector(0, 3)),
        Pixel("|", Vector(0, 4)),
        Pixel("|", Vector(0, 5)),
        
        Pixel("|", Vector(5, 1)),
        Pixel("|", Vector(5, 2)),
        Pixel("|", Vector(5, 3)),
        Pixel("|", Vector(5, 4)),
        Pixel("|", Vector(5, 5)),

        Pixel("-", Vector(1, 5)),
        Pixel("-", Vector(2, 5)),
        Pixel("-", Vector(3, 5)),
        Pixel("-", Vector(4, 5)),
    ])

    player_sprite = Sprite([
        Pixel("P")
    ])
# -------------------------------------------------
# Entities
# -------------------------------------------------
class Entity:
    def __init__(self, name : str, sprite : Sprite, position = Vector(0, 0)) -> None:
        self.name = name
        self.sprite = sprite
        self.position = position

class Fighter(Entity):
    def __init__(self, health : int, name : str, sprite : Sprite, position = Vector(0, 0)):
        self.health = health
        super().__init__(name, sprite, position)
# -------------------------------------------------
# Rooms
# -> list of all the rooms in the game
# -------------------------------------------------
class Room:
    def __init__(self, description = "this is a room lol", actions = ["action1", "action_2", "action 3"]) -> None:
        self.description = description
        self.actions = actions

    def enter(self, player : Fighter):
        greeting = player.name + " entered a room. \n"
        print(greeting + self.description)
        action = create_choice_prompt(self.actions)
        print(action)
        input("")
        clear()

# -------------------------------------------------
# Rendering
# -------------------------------------------------

screen_data = create_2d_array(__x, __y, ".")
space_string_memory : str

drawable_entity = []

def update_screen(space = " "):
    clear()
    reset_screen_buffer()

    global space_string_memory
    if space_string_memory == None:
        space_string_memory = space
    global screen_data

    global __x
    global __y

    drawable_entity.sort(key=evaluate_z_order)
    for e in drawable_entity:
        add_sprite_screen_buffer(e.sprite, e.position)

    for j in range(__y):
        for i in range(__x):
            print(screen_data[i][j], end=space_string_memory)
        print("")

def add_drawable_entity(entity : Entity):
    global drawable_entity
    drawable_entity.append(entity)

def evaluate_z_order(entity : Entity):
    return entity.sprite.z_index

def add_sprite_screen_buffer(sprite : Sprite, position : Vector):
    for pixel in sprite.pixels:
        newX = pixel.position.x + position.x
        newY = pixel.position.y + position.y
        if (newX < len(screen_data)) and (newY < len(screen_data[0])) and (newX >= 0) and (newY >= 0):
            screen_data[(pixel.position.x + position.x)][(pixel.position.y + position.y)] = pixel.character
    
def raw_draw(sprite : Sprite, position : Vector):
    add_sprite_screen_buffer(sprite, position)

    for i in range(__x):
        for j in range(__y):
            print(screen_data[i][j], end=" ")
        print("")
        
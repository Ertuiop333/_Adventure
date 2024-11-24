### Summary :
###     Definition of functions that are specific to rendering game visuals
###     These depend on visuals

import _Types as Types

import s_Terminal as Terminal


__render_queue = Types.Array()


class RenderObject:
    def __init__(self, sprite, position):
        self.sprite = sprite
        self.position = position


def add_object_to_render_queue(object: RenderObject):
    global __render_queue
    __render_queue.array.append(object)


def __write_render_object_to_screen_data(object: RenderObject):
    for pixel in object.sprite.pixels:
        newX = pixel.position.x + object.position.x
        newY = pixel.position.y + object.position.y
        if (
            (newX < len(Terminal.screen_data))
            and (newY < len(Terminal.screen_data[0]))
            and (newX >= 0)
            and (newY >= 0)
        ):
            Terminal.screen_data[(pixel.position.x + object.position.x)][
                (pixel.position.y + object.position.y)
            ] = pixel.character


def raw_draw(object: RenderObject):
    __write_render_object_to_screen_data(object)


def __evaluate_z_order(object: RenderObject):
    return object.sprite.z_index


def write_render_queue_to_screen_data():
    __render_queue.array.sort(key=__evaluate_z_order)
    for o in __render_queue.array:
        __write_render_object_to_screen_data(o)

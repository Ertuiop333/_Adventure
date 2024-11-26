import _Types as Types

import s_Visuals as Visuals
import s_Entities as Entities

import u_Components as Components
import u_Rendering as Rendering
import u_Physics as Physics

player = Entities.Entity(
    "Bob",
    Types.Vector(2, 2),
    [],
)

box = Entities.Entity(
    "box",
    Types.Vector(4, 4),
    [],
)


class InitData:
    def __init__(self, player: Entities.Entity, box: Entities.Entity):
        self.player = player
        self.box = box


def initialize() -> InitData:
    player.components = [
        Components.Renderer(player, Visuals.Sprite_Library.player_sprite),
        Components.Physic(player, Components.ColliderLibrary.single_point),
    ]

    box.components = [
        Components.Renderer(box, Visuals.Sprite_Library.default_square),
        Components.Physic(
            box,
            Components.ColliderLibrary.empty_box(6, 6),
        ),
    ]

    Rendering.add_object_to_render_queue(
        player.try_get_component_of_type(Components.Renderer)
    )
    Rendering.add_object_to_render_queue(
        box.try_get_component_of_type(Components.Renderer)
    )

    Physics.add_object_to_physics(player.try_get_component_of_type(Components.Physic))
    Physics.add_object_to_physics(box.try_get_component_of_type(Components.Physic))

    return InitData(player, box)

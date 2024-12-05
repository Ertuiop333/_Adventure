import _Types as Types

import s_Visuals as Visuals
import s_Entities as Entities

import u_Components as Components
import u_Rendering as Rendering
import u_Physics as Physics

player = Entities.Entity(
    "Bob",
    Types.Vector(0, 0),
    [],
)

grid = Entities.Entity(
    "box",
    Types.Vector(5, 3),
    [],
)


class ObjectsData:
    def __init__(self, player: Entities.Entity, box: Entities.Entity):
        self.player = player
        self.box = box


def generate() -> ObjectsData:
    player.components = [
        Components.Renderer(player, Visuals.Sprite_Library.player_sprite),
        Components.Renderer(player, Visuals.Sprite_Library.light_effect),
        Components.Physic(player, Components.ColliderLibrary.single_point),
    ]

    grid.components = [
        Components.Renderer(grid, Visuals.Sprite_Library.quadrier),
        Components.Physic(
            grid,
            Components.ColliderLibrary.empty_box(6, 6),
        ),
    ]

    Rendering.add_object_to_render_queue(
        player.try_get_components_of_type(Components.Renderer)[0]
    )
    Rendering.add_object_to_render_queue(
        player.try_get_components_of_type(Components.Renderer)[1]
    )

    Rendering.add_object_to_render_queue(
        grid.try_get_component_of_type(Components.Renderer)
    )

    Physics.add_object_to_physics(player.try_get_component_of_type(Components.Physic))
    Physics.add_object_to_physics(grid.try_get_component_of_type(Components.Physic))

    return ObjectsData(player, grid)

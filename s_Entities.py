# -------------------------------------------------
# Entity definition
# -------------------------------------------------
import _Types as Types


class Entity:
    def __init__(self, name: str, position: Types.Vector, components) -> None:
        self.name = name
        self.position = position
        self.components = components

    def try_get_component_of_type(self, type):
        for c in self.components:
            if isinstance(c, type):
                return c
        input(f"there is no component of type {type} in entity {self.name}")
        return None

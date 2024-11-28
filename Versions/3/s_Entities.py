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
    
    def try_get_components_of_type(self, type):
        l_components = []
        for c in self.components:
            if isinstance(c, type):
                l_components.append(c)
        if len(l_components) == 0 : 
            input(f"there is no component of type {type} on entity {self.name}")
        return l_components

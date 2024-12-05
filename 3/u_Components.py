import _Types as Types
import s_Entities as Entities
import s_Visuals as Visuals


class Component:
    def __init__(self, master_entity: Entities.Entity):
        self.master_entity = master_entity


# for rendering...
class Renderer(Component):
    def __init__(self, master_entity: Entities.Entity, sprite: Visuals.Sprite):
        super().__init__(master_entity)
        self.sprite = sprite


# for collision calculation
class Collider:
    def __init__(self, points: Types.Array, area: Types.Area):
        self.points = points
        self.area = area


class Physic(Component):
    def __init__(
        self,
        master_entity: Entities.Entity,
        collider: Collider,
    ):
        super().__init__(master_entity)
        self.collider = collider

# for easier assignment
class AreaLibrary:
    one_by_one = Types.Area(Types.Vector(0, 0), Types.Vector(0, 0))


class ColliderLibrary:
    single_point = Collider(
        Types.Array().new_1d_empty(1, Types.Vector(0, 0)),
        AreaLibrary.one_by_one,
    )

    def filled_box(x_size, y_size) -> Collider:
        points = Types.Array().new_2d_empty(x_size, y_size)

        if x_size == 0 or y_size == 0:
            input("error creating box collider : size is 0")
            return None

        for x in range(x_size):
            for y in range(y_size):
                points[x][y] = Types.Vector(x, y)

        return Collider(
            Types.convert_array_to_1d(points),
            Types.Area(Types.Vector(0, 0), Types.Vector(x_size - 1, y_size - 1)),
        )

    def empty_box(x_size, y_size) -> Collider:
        points = Types.Array().new_1d_empty(0, None)

        if x_size == 0 or y_size == 0:
            input("error creating box collider : size is 0")
            return None

        # two horizontal rows
        for x in range(x_size):
            points.append(Types.Vector(x, 0))
            points.append(Types.Vector(x, y_size - 1))

        # two vertical rows
        for y in range(1, y_size - 1):
            points.append(Types.Vector(0, y))
            points.append(Types.Vector(x_size - 1, y))

        return Collider(
            points,
            Types.Area(Types.Vector(0, 0), Types.Vector(x_size - 1, y_size - 1)),
        )

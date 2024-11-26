### Summary :
###     Definition of classes and functions that are specific to simulating game physics
###


import _Types as Types


class Area:
    def __init__(self, origin: Types.Vector, extent: Types.Vector):
        self.origin = origin
        self.extent = extent


class PointsCollider:
    def __init__(self, points: Types.Array, area: Area):
        # Array of vectors
        self.points = points
        self.area = area


class AreaLibrary:
    one_by_one = Area(Types.Vector(0, 0), Types.Vector(0, 0))


class ColliderLibrary:
    single_point = PointsCollider(
        Types.Array().new_1d_empty(1, Types.Vector(0, 0)),
        AreaLibrary.one_by_one,
    )


def filled_box(x_size, y_size) -> PointsCollider:
    points = Types.Array().new_2d_empty(x_size, y_size)

    if x_size == 0 or y_size == 0:
        input("error creating box collider : size is 0")
        return None

    for x in range(x_size):
        for y in range(y_size):
            points[x][y] = Types.Vector(x, y)

    return PointsCollider(
        Types.convert_array_to_1d(points),
        Area(Types.Vector(0, 0), Types.Vector(x_size - 1, y_size - 1)),
    )


def empty_box(x_size, y_size) -> PointsCollider:
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

    return PointsCollider(
        points,
        Area(Types.Vector(0, 0), Types.Vector(x_size - 1, y_size - 1)),
    )

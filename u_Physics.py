### Summary :
###     Definition of functions that are specific to simulating game physics
###     These depend on collision definition

import _Types as Types

import s_Collisions as Collisions


class PhysicsObject:
    def __init__(self, collider: Collisions.PointsCollider, position: Types.Vector):
        self.collider = collider
        self.position = position


__physics_objects = Types.Array().array


def add_object_to_physics(object: PhysicsObject):
    __physics_objects.append(object)


# tested
def __is_number_intersecting_range(number, range: Types.Vector) -> bool:
    high_boundary = range.y
    low_boundary = range.x

    if range.y < range.x:
        high_boundary = range.x
        low_boundary = range.y

    if number <= high_boundary and number >= low_boundary:
        return True
    else:
        return False


# tested
def __is_range1_intersecting_range2(range1: Types.Vector, range2: Types.Vector) -> bool:
    # check which one is the largest to exclude the possibility of including an entire range whitin the other
    larger = range2
    smaller = range1
    if abs(range1.y - range1.x) > abs(range2.y - range2.x):
        larger = range1
        smaller = range2

    if __is_number_intersecting_range(smaller.x, larger):
        return True
    if __is_number_intersecting_range(smaller.y, larger):
        return True
    return False


# tested
def __is_point_intersecting_area(point: Types.Vector, area: Collisions.Area) -> bool:
    # Checks if the point is within the box formed by the vector of the area
    #   |
    #   |
    #   |
    #   |_______A
    #   |      /|
    #   |     / |
    #   |    /  |
    #   |   /   |       2
    #   |  /    |
    #   | /    1|
    #   |/______|_______________________________________
    #
    # example: 1 is in and 2 is out

    x_axis_check = __is_number_intersecting_range(
        point.x, Types.Vector(area.origin.x, area.extent.x)
    )
    y_axis_check = __is_number_intersecting_range(
        point.y, Types.Vector(area.origin.y, area.extent.y)
    )

    if x_axis_check and y_axis_check:
        return True
    return False


# tested
def __is_area1_intersecting_with_area2(area1: Collisions.Area, area2: Collisions.Area):
    # Checks if the area is within the other area
    #   |
    #   |
    #   |
    #   |_______A1
    #   |      /|
    #   |     / |
    #   |    /  |
    #   |   /   |
    #   |__/____@________A2
    #   | /     |        |
    #   |/______|________|_______________________________

    x_axis_check = __is_range1_intersecting_range2(
        Types.Vector(area1.origin.x, area1.extent.x),
        Types.Vector(area2.origin.x, area2.extent.x),
    )
    y_axis_check = __is_range1_intersecting_range2(
        Types.Vector(area1.origin.y, area1.extent.y),
        Types.Vector(area2.origin.y, area2.extent.y),
    )

    if x_axis_check and y_axis_check:
        return True
    return False


def is_position_intersecting_with_object(
    position: Types.Vector, object: PhysicsObject
) -> bool:
    # first check if a collision is possible at the position in the collider's area
    if __is_point_intersecting_area(
        position,
        Collisions.Area(
            object.collider.area.origin + object.position,
            object.collider.area.extent + object.position,
        ),
    ):
        input("lol")
        # then check for individual points in the physics_object's collider
        for p in object.collider.points:
            if (p + object.position) == position:
                return True

    return False


def is_object_colliding_with_other_object(
    object1: PhysicsObject, object2: PhysicsObject
) -> bool:
    # first check if a collision is possible between the colliders by comparing their extents relative to their positions
    if __is_area1_intersecting_with_area2(
        Collisions.Area(
            object1.collider.area.origin + object1.position,
            object1.collider.area.extent + object1.position,
        ),
        Collisions.Area(
            object2.collider.area.origin + object2.position,
            object2.collider.area.extent + object2.position,
        ),
    ):
        # then check their individual points for intersection
        for p in object1.collider.points:
            if is_position_intersecting_with_object(p, object2):
                return True
    return False


def is_object_colliding_with_any_other_registered_object(object: PhysicsObject) -> bool:
    for o in __physics_objects:
        if is_object_colliding_with_other_object(o, object):
            return True
    return False

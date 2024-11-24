### Summary :
###     Definition of variable types that can be used like (int), (string) or similar
###     These don't depend on any game logic


# -------------------------------------------------
# Vector definition
# -------------------------------------------------
class Vector:
    def __init__(self, x=0, y=0):
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
# Nullable Array definition
# -------------------------------------------------
class Array:
    def new_1d_empty(self, first_d: int, default_value=None):
        self.array = [default_value for _ in range(first_d)]
        return self.array

    def new_2d_empty(self, first_d: int, second_d: int, default_value=None):
        self.array = [
            self.new_1d_empty(second_d, default_value) for _ in range(first_d)
        ]
        return self.array

    def __init__(self):
        self.array = self.new_1d_empty(0)

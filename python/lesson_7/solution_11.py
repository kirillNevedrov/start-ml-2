class Vector:
    def __init__(self, coords):
        self.coords = coords

    def __add__(self, other):
        if len(self.coords) != len(other.coords):
            raise ValueError(f"left and right lengths differ: {len(self.coords)} != {len(other.coords)}")

        return Vector([v_1 + v_2 for v_1, v_2 in zip(self.coords, other.coords)])

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector([v * other for v in self.coords])

        if isinstance(other, Vector):
            if len(self.coords) != len(other.coords):
                raise ValueError(f"left and right lengths differ: {len(self.coords)} != {len(other.coords)}")

            return sum([v_1 * v_2 for v_1, v_2 in zip(self.coords, other.coords)])
            
    def __abs__(self):
        return sum([v ** 2 for v in self.coords]) ** 0.5

    def __eq__(self, other):
        return (len(self.coords) == len(other.coords)) and all([v_1 == v_2 for v_1, v_2 in zip(self.coords, other.coords)])

    def __str__(self):
        return f"[{', '.join([str(c) for c in self.coords])}]"

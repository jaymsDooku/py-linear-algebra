import math
import matrix


class Vector:

    def __init__(self, *args, **kwargs):
        self.size = kwargs.get('size')
        self.contents = kwargs.get('contents', [0 for i in range(self.size)])

    def __getitem__(self, item):
        return self.contents[item]

    def __setitem__(self, key, value):
        self.contents[key] = value

    def __add__(self, other):
        result = Vector(self.size)

        for i in range(other.size):
            result.contents[i] += other.contents[i]

        return result

    def __sub__(self, other):
        result = Vector(self.size)

        for i in range(other.size):
            result.contents[i] -= other.contents[i]

        return result

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = Vector(self.size)
            for i in range(self.size):
                result.contents[i] = self.contents[i] * other
        elif isinstance(other, self.__class__):
            if self.size != other.size:
                raise ValueError("Tried to calculate inner product of incompatible vectors.")
            return sum([a * b for a, b in zip(self.contents, other.contents)])
        else:
            raise TypeError("Unsupported operand type.")

    def length(self):
        return math.sqrt(self.length_squared())

    def length_squared(self):
        return self * self

    def angle(self, other):
        theta = (self * other) / (self.length() * other.length())
        return math.acos(theta)

    def normalize(self):
        norm = Vector(self.size)
        length = self.length()
        norm.contents = [(self.contents[i] / length) for i in range(self.size)]
        return norm

    def to_matrix(self):
        result = matrix.Matrix(self.size, 1)
        result.set_col(0, self.contents)
        return result

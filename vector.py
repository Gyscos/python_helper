import math

class Vector:

    def __init__(self, dim):
        self.dim = dim
        self.data = list()

        for i in range(self.dim):
            self.data.append(0)

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def clone(self):
        result = Vector(self.dim)
        for i in range(self.dim):
            result[i] = self[i]
        return result

    def __iadd__(self, other):
        for i in range(self.dim):
            self[i] += other[i]
        return self

    def __add__(self, other):
        result = self.clone()
        result += other
        return result

    def __isub__(self, other):
        for i in range(dim):
            self[i] -= other[i]
        return self

    def __sub__(self, other):
        result = self.clone()
        result -= other
        return result

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            for i in range(self.dim):
                self[i] *= other
        return self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = self.clone()
            result *= other
            return result
        elif isinstance(other, Vector):
            s = 0
            if self.dim == other.dim:
                for i in range(self.dim):
                    s += self[i] * other[i]
            return s


    def sq_length(self):
        return self * self

    def length(self):
        return math.sqrt(self.sq_length())


v = Vector(3)
v[0] = 0
v[2] = 4
v[1] = 3

v += v
v *= 2

print(v.length())

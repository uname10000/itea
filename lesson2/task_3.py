class Point:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_z(self):
        return self._z

    def set_x(self, value):
        self._x = value

    def set_y(self, value):
        self._y = value

    def set_z(self, value):
        self._z = value

    def __add__(self, other):
        return Point(self._x + other.get_x(), self._y + other.get_y(), self._z + other.get_z())

    def __sub__(self, other):
        return Point(self._x - other.get_x(), self._y - other.get_y(), self._z - other.get_z())

    def __mul__(self, other):
        return Point(self._x * other.get_x(), self._y * other.get_y(), self._z * other.get_z())

    def __truediv__(self, other):
        return Point(int(self._x / other.get_x()), int(self._y / other.get_y()), int(self._z / other.get_z()))

    def __imul__(self, other):
        return Point(self._x * other.get_x(), self._y * other.get_y(), self._z * other.get_z())

    def __neg__(self):
        return Point(-self._x, -self._y, -self._z)


def show_point(text, point):
    print(f'{text}: x:{point.get_x()} y:{point.get_y()} z:{point.get_z()}')


point1 = Point(10, 20, 30)
point2 = Point(2, 5, 9)

show_point('point1', point1)
show_point('point2', point2)


result = point1 + point2
show_point('__add__', result)

result = point1 - point2
show_point('__sub__', result)

result = point1 * point2
show_point('__mul__', result)

result = point1 / point2
show_point('__div__', result)

print('-'*20)
print('-'*20)
point1.set_x(1)
point1.set_y(2)
point1.set_z(3)

point2.set_x(1)
point2.set_y(2)
point2.set_z(3)

result = point1 * point2
show_point('point1', point1)
show_point('point2', point2)
show_point('__mul__', result)

print('-'*20)
result = -point1
show_point('__neg__', result)
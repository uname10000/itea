class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b > 0:
            return f'{self.a} + {self.b}i'
        elif self.b == 0:
            return f'{self.a}'
        else:
            return f'{self.a} - {abs(self.b)}i'

    def __add__(self, other):
        return ComplexNum(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return ComplexNum(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        a = self.a * other.a - self.b * other.b
        b = self.b * other.a + self.a * other.b
        return ComplexNum(a, b)

    def __truediv__(self, other):
        a = (self.a * other.a + self.b * other.b) / (other.a ** 2 + other.b ** 2)
        b = (self.b * other.a - self.a * other.b) / (other.a ** 2 + other.b ** 2)
        return ComplexNum(a, b)


c1 = ComplexNum(13, 1)
c2 = ComplexNum(7, 6)

print(f'c1: {c1}')
print(f'c2: {c2}')

result = c1 + c2
print(f'add: {result}')

result = c1 - c2
print(f'sub: {result}')

result = c1 * c2
print(f'mul: {result}')

result = c1 / c2
print(f'div: {result}')

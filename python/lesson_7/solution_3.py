class Triangle:
    n_dots = 3

    def __init__(self, a, b, c):
        if (a > b + c) or (b > a + c) or (c > a + b):
            raise ValueError("triangle inequality does not hold")

        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

class Rectangle(Triangle):
    n_dots = 4

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

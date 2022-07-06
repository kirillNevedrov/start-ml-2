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

tr_1 = Triangle(2, 2, 3)
tr_2 = Triangle(2, 2, 3)

square_1 = tr_1.area()
square_2 = tr_2.area()

class BaseFigure:
    n_dots = None

    def __init__(self):
        self.validate()

    def validate(self):
        raise NotImplementedError 

    def area(self):
        raise NotImplementedError

class Triangle(BaseFigure):
    n_dots = 3

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        super().__init__()

    def validate(self):
        if (self.a > self.b + self.c) or (self.b > self.a + self.c) or (self.c > self.a + self.b):
            raise ValueError("triangle inequality does not hold")

        return self.a, self.b, self.c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

class Rectangle(BaseFigure):
    n_dots = 4

    def __init__(self, a, b):
        self.a = a
        self.b = b

        super().__init__()

    def validate(self):
        return self.a, self.b

    def area(self):
        return self.a * self.b
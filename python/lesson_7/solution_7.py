class BaseFigure:
    n_dots = None

    def __init__(self):
        self.validate()

    def validate(self):
        raise NotImplementedError 

    def area(self):
        raise NotImplementedError

class Circle(BaseFigure):
    n_dots = float('inf')

    def __init__(self, r):
        self.r = r

        super().__init__()

    def validate(self):
        return self.r

    def area(self):
        return 3.14 * (self.r ** 2)
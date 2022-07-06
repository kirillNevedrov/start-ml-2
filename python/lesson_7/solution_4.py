class BaseFigure:
    n_dots = None

    def __init__(self):
        self.validate()

    def validate(self):
        raise NotImplementedError 

    def area(self):
        raise NotImplementedError

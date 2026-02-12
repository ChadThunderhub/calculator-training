class Division:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        if self.b == 0:
            raise ValueError("Nie można dzielić przez zero.")
        return self.a / self.b
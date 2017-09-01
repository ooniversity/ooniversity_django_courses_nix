
class Quadratic:
    def __init__(self, a, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        self.desc = self.get_desc()

    def get_desc(self):
        return self.b ** 2 - 4 * self.a * self.c

    def get_x1(self):
        x1 = (-self.b + self.desc ** (1 / 2.0)) / 2 * self.a
        return x1

    def get_x2(self):
        x2 = (-self.b - self.desc ** (1 / 2.0)) / 2 * self.a
        return x2


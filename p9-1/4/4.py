class Progression:
    def __init__(self, start, step):
        self.start = start
        self.step = step

    def __iter__(self):
        return self

class ArithmeticProgression(Progression):
    def __next__(self):
        value = self.start
        self.start += self.step
        return value

class GeometricProgression(Progression):
    def __next__(self):
        value = self.start
        self.start *= self.step
        return value

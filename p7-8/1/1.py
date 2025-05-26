class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'
    
class Circle:
    def __init__(self, radius, center):
        self.center = center
        self.radius = radius

    def __str__(self):
        return f'{self.center}, r = {self.radius}'
    
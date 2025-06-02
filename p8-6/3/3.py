from dataclasses import dataclass, field

@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0
    quadrant: int = field(init=False)

    def __post_init__(self):
        self.quadrant = 0
        if self.x > 0:
            if self.y > 0:
                self.quadrant = 1
            elif self.y < 0:
                self.quadrant = 4
        elif self.x < 0:
            if self.y > 0:
                self.quadrant = 2
            elif self.y < 0:
                self.quadrant = 3

    def symmetric_x(self):
        return Point(self.x, -self.y)

    def symmetric_y(self):
        return Point(-self.x, self.y)


from functools import total_ordering

@total_ordering
class Shape:
    __slots__ = ('name', 'color', 'area')

    def __init__(self, name, color, area):
        self.name = name
        self.color = color
        self.area = area

    def __eq__(self, value):
        if isinstance(value, Shape):
            return self.area == value.area
        return NotImplemented
    
    def __ge__(self, value):
        if isinstance(value, Shape):
            return self.area > value.area
        return NotImplemented
        
    def __str__(self):
        return f'{self.color} {self.name} ({self.area})'
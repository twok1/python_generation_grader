class ColoredPoint:
    def __init__(self, x, y, color) -> None:
        self._x = x
        self._y = y
        self._color = color
        
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def color(self):
        return self._color
    
    @property
    def fields(self):
        return self.x, self.y, self.color
    
    def __repr__(self) -> str:
        return f"ColoredPoint({self.x}, {self.y}, '{self.color}')"
        
    def __hash__(self) -> int:
        return hash(self.fields)
        
    def __eq__(self, other):
        if isinstance(other, ColoredPoint):
            return self.fields == other.fields
        return NotImplemented
        
    def __ne__(self, other):
        if isinstance(other, ColoredPoint):
            return self.fields != other.fields
        return NotImplemented
    
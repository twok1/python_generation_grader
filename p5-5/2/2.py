class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self) -> str:
        return f'Vector({self.x}, {self.y})'
    
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
        
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __rsub__(self, other):
        return self.__sub__(other)
        
    def __mul__(self, other):
        if isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other)
        return NotImplemented
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        if isinstance(other, (float, int)):
            return Vector(self.x / other, self.y / other)
        return NotImplemented
    
    def __rtruediv__(self, other):
        return self.__div__(other)

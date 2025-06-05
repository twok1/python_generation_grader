from math import sqrt

class Vector:
    def __init__(self, *args):
        self.coords = args
        self.__ne__ = self.__eq__

    def __str__(self):
        return str(self.coords)
    
    def __len__(self):
        return len(self.coords)
    
    def _check_for_len(self, value):
        if len(self) == len(value.coords):
             return True
        raise ValueError('Векторы должны иметь равную длину')
    
    def _arythmetic_operation(self, value, operation, all_sums=False):
        if isinstance(value, Vector):
            self._check_for_len(value)
            result = tuple(operation(i, k) for i, k in zip(self.coords, value.coords))
            return Vector(*result) if not all_sums else sum(result)
        return NotImplemented
    
    def __add__(self, value):
        return self._arythmetic_operation(value, lambda x, y: x + y)
    
    def __sub__(self, value):
        return self._arythmetic_operation(value, lambda x, y: x - y)
    
    def __mul__(self, value):
        return self._arythmetic_operation(value, lambda x, y: x * y, all_sums=True)
    
    def norm(self):
        return sqrt(sum(i**2 for i in self.coords))

    def __eq__(self, value):
        if isinstance(value, Vector):
            self._check_for_len(value)
            return self.coords == value.coords

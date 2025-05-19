from collections import UserList


class NumberList(UserList):
    def __init__(self, iterable=[]):
        super().__init__(self._check_num(i) for i in iterable)
    
    def append(self, item):
        self.data.append(self._check_num(item))

    def __add__(self, other):
        if type(other) in (list, tuple, NumberList):
            return super().__add__(self._check_num(i) for i in other)
        
    def __iadd__(self, other):
        if type(other) in (list, NumberList):
            return super().__iadd__(self._check_num(i) for i in other)
    
    def __setitem__(self, key, item):
        self._check_num(item)
        self.data.__setitem__(key, item)

    def insert(self, i, item):
        return super().insert(i, self._check_num(item))
    
    def extend(self, other):
        return super().extend(self._check_num(i) for i in other)
        
    def _check_num(self, num):
        if type(num) not in (int, float):
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        return num

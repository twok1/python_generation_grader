from random import randint

class RandomNumber:
    def __set_name__(self, cls, attr):
        self._attr = attr

    def __init__(self, start, end, cache=False):
        self._start = start
        self._end = end
        self._cache = cache
        self._number = randint(start, end)

    def __get__(self, obj, cls):    
        if obj is None:
            return self
        if self._cache:
            return self._number
        return randint(self._start, self._end)
    
    def __set__(self, obj, value):
        raise AttributeError("Изменение невозможно")
            
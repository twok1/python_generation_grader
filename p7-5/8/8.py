from collections.abc import MutableSequence


class SortedList(MutableSequence):
    def __init__(self, iterable=[]):
        self._iterable = list(i for i in iterable)

    @property
    def iterable(self):
        return list(sorted(self._iterable))
    
    def __repr__(self):
        return f'SortedList({self.iterable})'
    
    def add(self, value):
        self._iterable.append(value)

    def discard(self, value):
        while value in self._iterable:
            self._iterable.remove(value)

    def update(self, value):
        self._iterable.extend(value)
    
    def __len__(self):
        return len(self._iterable)
    
    def __contains__(self, value):
        return value in self._iterable
    
    def pop(self, index = -1):
        return NotImplemented
    
    def __getitem__(self, index):
        return self.iterable[index]
    
    def __add__(self, other):
        if isinstance(other, SortedList):
            return SortedList(self.iterable + other.iterable)
        return NotImplemented
    
    def __iadd__(self, values):
        if isinstance(values, SortedList):
            self._iterable += values._iterable
            return self
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, int):
            return SortedList(self.iterable * other)
        return NotImplemented
    
    def __imul__(self, other):
        if isinstance(other, SortedList) or isinstance(other, int):
            self._iterable *= other
            return self
        return NotImplemented
    
    def __getitem__(self, index):
        return self.iterable[index]
    
    def __delitem__(self, index):
        self._iterable.remove(self.iterable[index])

    def __setitem__(self, index, value):
        raise NotImplementedError

    def append(self, value):
        raise NotImplementedError
    
    def insert(self, index, value):
        raise NotImplementedError
    
    def extend(self, values):
        raise NotImplementedError
    
    def __reversed__(self):
        raise NotImplementedError
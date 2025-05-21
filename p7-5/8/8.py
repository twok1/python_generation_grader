from collections.abc import MutableSequence


class SortedList(MutableSequence):
    def __init__(self, iterable):
        self._iterable = list(i for i in iterable)

    @property
    def iterable(self):
        return list(sorted(self._iterable))
    
    def __repr__(self):
        return f'SortedList({self.iterable})'
    
    def add(self, value):
        self._iterable += list(value)

    def discard(self, value):
        self._iterable.remove(list(value))

    def update(self, value):
        self.iterable.extend(value)

    def __reversed__(self):
        raise NotImplemented
    
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
    
    def __imul__(self, other):
        if isinstance(other, int):
            return SortedList(i * other for i in self.iterable)
        return NotImplemented
    
numbers = SortedList([5, 3, 4, 2, 1])


print(numbers)
print(numbers[1])
print(numbers[-2])
numbers.add(0)
print(numbers)
numbers.discard(4)
print(numbers)
numbers.update([4, 6])
print(numbers)
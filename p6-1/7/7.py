
class LoopTracker:
    def __init__(self, iterable):
        self.l = len(iterable)
        iterable = tuple(iterable)
        self.iterable = iter(iterable)
        self._accesses = 0
        self._empty_accesses = 0
        if iterable:
            self.empty = False
            self._first = iterable[0]
            self._last = None
        else:
            self.empty = True
            self._first = None
            self._last = None
        
    def __iter__(self):
        return self.iterable
    
    def __next__(self):
        try:
            self._last = next(self.iterable)
            self._accesses += 1
            if self.accesses == self.l:
                self.empty = True
            return self._last
        except StopIteration:
            self._empty_accesses += 1
            self.empty = True
            
            
    @property
    def first(self):
        if self.l > 0:
            return self._first
        else:
            raise AttributeError('Исходный итерируемый объект пуст')
    
    @property
    def empty_accesses(self):
        return self._empty_accesses
    
    @property
    def accesses(self):
        return self._accesses
    
    @property
    def last(self):
        if self._last:
            return self._last
        else:
            raise AttributeError('Последнего элемента нет')
    
    def is_empty(self):
        return self.empty
    
loop_tracker = LoopTracker(dict.fromkeys(range(100)))

print(next(loop_tracker))
print(next(loop_tracker))
print(next(loop_tracker))
print(loop_tracker.accesses)
print(loop_tracker.first)
print(loop_tracker.last)
print(loop_tracker.is_empty())
class OrderedSet:
    def __init__(self, iterable=()):
        self.iterable = dict.fromkeys(iterable)
        
    def add(self, value):
        self.iterable.update(dict.fromkeys((value,)))
    
    def discard(self, value):
        if value in self.iterable:
            self.iterable.pop(value)
        
    def __iter__(self):
        return iter(self.iterable.keys())
    
    def __len__(self):
        return len(self.iterable)
    
    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return tuple(self.iterable) == tuple(other.iterable)
        if isinstance(other, set):
            return (set(self.iterable.keys())) == other
        return NotImplemented
    
    def __ne__(self, other):
        if isinstance(other, OrderedSet):
            return tuple(self.iterable) != tuple(other.iterable)
        if isinstance(other, set):
            return (set(self.iterable.keys())) != other
        return NotImplemented
    
    
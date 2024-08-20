class Peekable:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        return next(self.iterable)
    
    def peek(self, default='s'):
        prev_iterable = tuple(self.iterable)
        try:
            k = prev_iterable[0]
        except IndexError:
            if default != 's':
                return default
            else:
                raise StopIteration
        self.iterable = iter(prev_iterable)
        return k
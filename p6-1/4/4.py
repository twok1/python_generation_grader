class SkipIterator:
    def __init__(self, iterable, n):
        self.iterable = tuple(val for num, val in enumerate(iterable) if not num % (n + 1))
        self.ind = 0
        
    def __iter__(self):
        return iter(self.iterable)
    
    def __next__(self):
        if self.ind == len(self.iterable):
            raise StopIteration
        else:
            self.ind += 1
            return self.iterable[self.ind - 1]

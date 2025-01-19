class CyclicList:
    def __init__(self, iterable=[]):
        self.iterable = list(iterable)
        
    def append(self, value):
        self.iterable.append(value)
        
    def pop(self, key=None):
        if isinstance(key, int):
            return self.iterable.pop(key % len(self))
        return self.iterable.pop()
    
    def __len__(self):
        return len(self.iterable)
    
    def __getitem__(self, key):
        return self.iterable[key % len(self)]
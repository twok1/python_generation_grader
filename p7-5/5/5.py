from collections.abc import Sequence


class CustomRange(Sequence):
    def __init__(self, *args):
        self.values = []
        for i in args:
            if isinstance(i, int):
                self.values.append(i)
            else:
                self.values.extend(range(int(i.split('-')[0]), int(i.split('-')[1]) + 1))
    
    def __contains__(self, value):
        return value in self.values
    
    def __iter__(self):
        return iter(self.values)
    
    def __reversed__(self):
        return reversed(self.values)
    
    def index(self, value, start = 0, stop = ...):
        return self.values.index(value, start, stop)
    
    def count(self, value):
        return self.values.count(value)
    
    def __getitem__(self, index):
        return self.values[index]
    
    def __len__(self):
        return len(self.values)

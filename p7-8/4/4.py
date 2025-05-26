from collections import OrderedDict

class Queue:
    def __init__(self, pairs=None):
        self.pairs = OrderedDict()
        if pairs:
            self.pairs.update(pairs)

    def add(self, value: tuple):
        k, v = value
        if k in self.pairs:
            self.pairs.move_to_end(k)
        self.pairs[k] = v

    def pop(self):
        if self.pairs:
            return self.pairs.popitem(last=False)
        raise KeyError('Очередь пуста')
    
    def __len__(self):
        return len(self.pairs)
    
    def __repr__(self):
        return f'Queue({list(self.pairs.items())})'

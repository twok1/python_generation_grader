from collections.abc import Sequence


class BitArray(Sequence):
    def __init__(self, values=[]):
        self.values = list(values)

    def __getitem__(self, index):
        return self.values[index]
    
    def __len__(self):
        return len(self.values)
    
    def __repr__(self):
        return str(self.values)
    
    def __reversed__(self):
        return reversed(self.values)
    
    def __invert__(self):
        return BitArray([0 if i == 1 else 1 for i in self.values ])

    def __or__(self, value):
        if isinstance(value, BitArray):
            if len(self) == len(value):
                return BitArray([i | k for i, k in zip(self, value)])
        return NotImplemented
            
    def __and__(self, value):
        if isinstance(value, BitArray):
            if len(self) == len(value):
                return BitArray([i & k for i, k in zip(self, value)])
        return NotImplemented
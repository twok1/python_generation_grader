from collections.abc import Sequence


class DNA(Sequence):
    COMPL = {
        'A': 'T',
        'G': 'C',
        'T': 'A',
        'C': 'G',
    }
    def __init__(self, chain):
        self.chain = chain

    def __getitem__(self, index):
        return (self.chain[index], self.COMPL[self.chain[index]])
    
    def __len__(self):
        return len(self.chain)
    
    def __str__(self):
        return self.chain
    
    def __contains__(self, value):
        return value in self.chain
    
    def __add__(self, other):
        if isinstance(other, DNA):
            return DNA(self.chain + other.chain)
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, DNA):
            return self.chain == other.chain
        return NotImplemented
        
    def __ne__(self, other):
        if isinstance(other, DNA):
            return self.chain != other.chain
        return NotImplemented
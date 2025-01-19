class ReversedSequence:
    def __init__(self, sequence) -> None:
        self.first_sequence = sequence
        
    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError
        if 0 <= key <= len(self.first_sequence):
            return tuple(reversed(self.first_sequence))[key]
        raise ValueError
    
    def __len__(self):
        return len(self.first_sequence)
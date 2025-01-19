class SequenceZip:
    def __init__(self, *args):
        self.sequence = tuple(zip(*args))
        
    def __getitem__(self, key):
        return self.sequence[key]
    
    def __len__(self):
        return len(self.sequence)
    
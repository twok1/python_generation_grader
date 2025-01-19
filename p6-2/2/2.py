class SparseArray:
    def __init__(self, default) -> None:
        self.sequence = []
        self.default = default
        
    def check_for_len(self, key):
        while len(self) <= key:
            self.sequence += [self.default]
        
        
    def __getitem__(self, key):
        self.check_for_len(key)
        return self.sequence[key]
            
    def __setitem__(self, key, value):
        self.check_for_len(key)
        self.sequence[key] = value
        
    def __len__(self):
        return len(self.sequence)
    
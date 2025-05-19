class ValueDict(dict):
    def __init__(self, d):
        return super().__init__(d)
    
    def key_of(self, value):
        for k, v in self.items():
            if v == value:
                return k
        return None
    
    def keys_of(self, value):
        return (k for k, v in self.items() if v == value)
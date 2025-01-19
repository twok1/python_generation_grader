class MutableString:
    def __init__(self, string: str = '') -> None:
        self.string = string
        
    def upper(self):
        self.string = self.string.upper()
    
    def lower(self):
        self.string = self.string.lower()
    
    def __str__(self) -> str:
        return self.string
    
    def __repr__(self) -> str:
        return f"MutableString('{self.string}')"
    
    def __len__(self):
        return len(self.string)
    
    def __iter__(self):
        return iter(self.string)
    
    def __getitem__(self, key):
        return MutableString(self.string[key])
    
    def __setitem__(self, key, value):
        data = (list(self.string))
        data[key] = value
        self.string = ''.join(data)
        
    def __delitem__(self, key):
        data = (list(self.string))
        del data[key]
        self.string = ''.join(data)
        
    def __add__(self, other):
        if isinstance(other, MutableString):
            return MutableString(self.string + other.string)
    
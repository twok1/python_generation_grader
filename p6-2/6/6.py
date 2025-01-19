class PermaDict:
    def __init__(self, data: dict={}):
        self.data = data.copy()
        
    def keys(self):
        return iter(self.data.keys())
    
    def values(self):
        return iter(self.data.values())
    
    def items(self):
        return (self.data.items())
    
    def __len__(self):
        return len(self.data)
    
    def __iter__(self):
        return iter(self.data)
    
    def __setitem__(self, key, value):
        if key in self.data:
            raise KeyError('Изменение значения по ключу невозможно')
        else:
            self.data[key] = value
    
    def __getitem__(self, key):
        return self.data[key]
    
    def __delitem__(self, key):
        del self.data[key]

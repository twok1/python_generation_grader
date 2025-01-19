class HistoryDict:
    def __init__(self, data: dict={}) -> None:
        self.data = data.copy()
        self.history_data = {}
        for k, v in data.items():
            self.history_data[k] = [v]
        
    def keys(self):
        return iter(self.data.keys())
    
    def values(self):
        return iter(self.data.values())
    
    def items(self):
        return iter(self.data.items())
    
    def history(self, key):
        if key in self.history_data:
            return self.history_data[key]
        else:
            return []
    
    def all_history(self):
        return {k: self.history_data[k] for k in self.data}
    
    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        self.data[key] = value
        if key in self.history_data:
            self.history_data[key].append(value)
        else:
            self.history_data[key] = [value]
        
    def __delitem__(self, key):
        del self.data[key]
        del self.history_data[key]
    
    def __len__(self):
        return len(self.data)
    
    def __iter__(self):
        return iter(self.data)

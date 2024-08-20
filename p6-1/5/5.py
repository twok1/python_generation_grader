class RandomLooper:
    def __init__(self, *args):
        self.obj = iter(sum(list(map(list, (args))), []))
        
    def __iter__(self):
        return self
    
    def __next__(self):
        return next(self.obj)
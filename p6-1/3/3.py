class AttrsIterator:
    def __init__(self, obj):
        self.obj = list((k, v) for k, v in obj.__dict__.items())
        self.ind = 0
        
    def __iter__(self):
        return iter(self.obj)
    
    def __next__(self):
        if self.ind == len(self.obj):
            raise StopIteration 
        else:
            self.ind += 1
            return self.obj[self.ind - 1]


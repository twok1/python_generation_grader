class CachedFunction:
    def __init__(self, func):
        self.func = func
        self.cache = {}
        
    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        result = self.func(*args)
        self.cache[args] = result
        return result
        
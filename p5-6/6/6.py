class Filter:
    def __init__(self, predicate):
        self.predicate = predicate
        
    def __call__(self, iterable):
        return list(filter(self.predicate, iterable))
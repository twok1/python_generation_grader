class Grouper:
    def __init__(self, iterable, key) -> None:
        self.iterable: dict = {}
        self.key = key
        for i in iterable:
            self._find_and_insert(i)
    
    def _find_and_insert(self, item):
        key = self.key(item)
        self.iterable.setdefault(key, []).append(item)
    
    def add(self, item):
        self._find_and_insert(item=item)
    
    def group_for(self, value):
        return self.key(value)
    
    def __len__(self):
        return len(self.iterable)
    
    def __iter__(self):
        return iter(self.iterable.items())
    
    def __getitem__(self, key):
        return self.iterable[key]
    
    def __contains__(self, key):
        return key in self.iterable

class Queue:
    def __init__(self, *args):
        self.queue = list(args)
        
    def __str__(self) -> str:
        return ' -> '.join(map(str, self.queue))
    
    def add(self, *args):
        self.queue += list(args)
        
    def pop(self):
        if self.queue:
            return self.queue.pop(0)
        return None
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Queue):
            return self.queue == value.queue
        
    def __ne__(self, value: object) -> bool:
        if isinstance(value, Queue):
            return self.queue != value.queue
        
    def __add__(self, other):
        if isinstance(other, Queue):
            return Queue(*(self.queue + other.queue))
        return NotImplemented
        
    def __iadd__(self, other):
        if isinstance(other, Queue):
            self.queue += other.queue
            return self
        return NotImplemented
    
    def __rshift__(self, value):
        if isinstance(value, int):
            return Queue(*self.queue[value:])
        return NotImplemented
    

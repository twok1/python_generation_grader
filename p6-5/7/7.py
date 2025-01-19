class Suppress:
    def __init__(self, *args) -> None:
        self.exceptions = args
        self.exception = None
        
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        for variable in self.exceptions:
            if variable == exc_type:
                self.exception = exc_value
                return True
        return False
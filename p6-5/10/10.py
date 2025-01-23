from time import perf_counter

class AdvancedTimer:
    def __init__(self):
        self.runs = []
        self.last_run = None
        self.min = None
        self.max = None

    def __enter__(self):
        self.start = perf_counter()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.last_run = perf_counter() - self.start
        self.runs.append(self.last_run)
        self.max = max(self.runs)
        self.min = min(self.runs)
        return True
    
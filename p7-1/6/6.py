class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, val=1):
        self.value += val
        self.check_val()

    def dec(self, val=1):
        self.value -= val
        self.check_val()
    
    def check_val(self):
        if self.value < 0:
            self.value = 0

class NonDecCounter(Counter):
    def dec(self, val=1):
        pass

class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        super().__init__(start)
        self._limit = limit

    def check_val(self):
        super().check_val()
        if self.value > self._limit:
            self.value = self._limit

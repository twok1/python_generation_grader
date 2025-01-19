from copy import copy, deepcopy


class Atomic:
    def __init__(self, data, deep=False):
        self.data = data
        if deep:
            self.start_data = deepcopy(data)
        else:
            self.start_data = copy(data)

    def __enter__(self):
        return self.data
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.data = self.start_data
            return False
        return True

numbers = [1, 2, 3, 4, 5]

with Atomic(numbers) as atomic:
    atomic.append(6)
    atomic[2] = 0
    del atomic[100]           # обращение по несуществующему индексу

print(numbers)
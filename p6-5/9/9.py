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
            if isinstance(self.data, list):
                self.data[:] = self.start_data[:]
            if isinstance(self.data, dict|set):
                self.data.clear()
                self.data.update(self.start_data)
            return True

        return True

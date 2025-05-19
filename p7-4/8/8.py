from collections import UserString


class MutableString(UserString):
    def __init__(self, seq):
        super().__init__(seq)

    def lower(self):
        self.data = self.data.lower()
        return super().lower()

    def upper(self):
        self.data = self.data.upper()
        return super().upper()
    
    def sort(self, key=None, reverse=False):
        self.data = ''.join(sorted(tuple(self.data), key=key, reverse=reverse))

    def __setitem__(self, index, item):
        self.data = self.data[:index] + item + self.data[index + 1:]
    
    def __delitem__(self, index):
        index = index if index >= 0 else len(self.data) + index
        self.data = self.data[:index] + self.data[index + 1:]

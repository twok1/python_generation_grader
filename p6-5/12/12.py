from collections import defaultdict
import copy


class TreeBuilder:

    def __init__(self):
        self.tree = defaultdict(list)
        self.level = 0

    def add(self, val):
        self.tree[self.level].append(val)

    def structure(self):
        return self.tree[0]

    def __enter__(self):
        self.level += 1
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        temp = copy.copy(self.tree[self.level])
        self.tree[self.level] = []
        self.level -= 1
        if temp:
            self.tree[self.level] += [temp]
        return True

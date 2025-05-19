from collections import UserList

class AdvancedList(UserList):
    def join(self, joiner=' '):
        return str(joiner).join(map(str, self.data))
    
    def map(self, func):
        self.data = list(map(func, self.data))

    def filter(self, func):
        self.data = list(filter(func, self.data))


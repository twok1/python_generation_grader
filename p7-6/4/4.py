class Human:
    def __init__(self, mood='neutral'):
        self.mood = mood

class Father(Human):
    def greet(self):
        return 'Hello!'
    
    def be_strict(self):
        self.mood = 'strict'

class Mother(Human):
    def greet(self):
        return 'Hi, honey!'
    
    def be_kind(self):
        self.mood = 'kind'

class Daughter(Mother, Father):
    pass

class Son(Father, Mother):
    pass


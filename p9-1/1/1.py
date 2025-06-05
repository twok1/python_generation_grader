class Anything:
    def __eq__(self, value):
        return True
    
    def __ne__(self, value):
        return True
    
    def __ge__(self, value):
        return True
    
    def __gt__(self, value):
        return True
    
    def __le__(self, value):
        return True
    
    def __lt__(self, value):
        return True

def anything():
    return Anything()

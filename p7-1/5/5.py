class Validator:
    def __init__(self, obj):
        self._obj = obj

    def is_valid(self):
        return None
    
class NumberValidator(Validator):
    def is_valid(self):
        return type(self._obj) in (int, float)
    
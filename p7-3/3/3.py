class FuzzyString(str):
    def __eq__(self, value):
        if type(value) in (str, FuzzyString):
            return super().lower().__eq__(value.lower())
        return NotImplemented
    
    def __ne__(self, value):
        if type(value) in (str, FuzzyString):
            return super().lower().__ne__(value.lower())
        return NotImplemented
    
    def __lt__(self, value):
        if type(value) in (str, FuzzyString):
            return super().lower().__lt__(value.lower())
        return NotImplemented
    
    def __gt__(self, value):
        if type(value) in (str, FuzzyString):
            return super().lower().__gt__(value.lower())
        return NotImplemented

    def __ge__(self, value):
        if type(value) in (str, FuzzyString):
            return super().lower().__ge__(value.lower())
        return NotImplemented
    
    def __le__(self, value):
        if type(value) in (str, FuzzyString):
            return super().lower().__le__(value.lower())
        return NotImplemented
    
    def __contains__(self, key):
        if type(key) in (str, FuzzyString):
            return super().lower().__contains__(key.lower())
        return NotImplemented
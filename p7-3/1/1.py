class UpperPrintString(str):
    def __new__(cls, string):
        return super().__new__(cls, string)
    
    def __str__(self):
        return super().__str__().upper()
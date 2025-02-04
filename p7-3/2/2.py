class LowerString(str):
    def __new__(cls, obj=''):
        return super().__new__(cls, str(obj).lower())
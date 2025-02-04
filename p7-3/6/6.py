class RoundedInt(int):
    def __new__(cls, num, even=True):
        return super().__new__(cls, num + (num % 2 == even))
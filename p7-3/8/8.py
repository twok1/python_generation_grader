class ModularTuple(tuple):
    def __new__(cls, iterable, size=100):
        iterable = tuple(map(lambda x: x / size, iterable))
        super().__new__(cls, iterable)


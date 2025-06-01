import functools

class type_check:
    def __init__(self, types: list):
        self.types = types

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            i = 0
            while i < min(len(self.types), len(args)):
                if not isinstance(args[i], self.types[i]):
                    raise TypeError
                i += 1
            return func(*args, **kwargs)
        return wrapper

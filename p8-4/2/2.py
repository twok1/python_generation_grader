import functools

class MaxCallsException(Exception):
    pass

class limited_calls:
    def __init__(self, n):
        self.n = n

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if self.n == 0:
                raise MaxCallsException('Превышено допустимое количество вызовов')
            self.n -= 1
            return func(*args, **kwargs)
        return wrapper
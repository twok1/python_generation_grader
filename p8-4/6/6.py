import functools

class ignore_exception:
    def __init__(self, *args):
        self.exceptions = args
    
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if type(e) in self.exceptions:
                    print(f'Исключение {e.__class__.__name__} обработано')
                return e.__class__.__name__
        return wrapper
    
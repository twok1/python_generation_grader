import functools

class exception_decorator:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwds):
        try:
            return (self.func(*args, **kwds), None)
        except Exception as e:
            return (None, type(e))
import functools

class reverse_args:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwds):
        return self.func(*reversed(args), **kwds)
    
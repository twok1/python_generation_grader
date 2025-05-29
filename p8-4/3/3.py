import functools

class takes_numbers:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwds):
        for i in args + tuple(kwds.values()):
            if type(i) not in (int, float):
                raise TypeError('Аргументы должны принадлежать типам int или float')
        return self.func(*args, **kwds)
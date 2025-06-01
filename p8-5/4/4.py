import functools

def singleton(cls):
    old_new = cls.__new__
    cls._instance = None

    @functools.wraps(old_new)
    def new_new(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = old_new(cls)
        return cls._instance

    cls.__new__ = new_new
    return cls

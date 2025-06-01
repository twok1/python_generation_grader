from collections import OrderedDict
import functools

def limiter(limit: int, unique: str, lookup: str):
    def wrapper(cls):
        cls.instances = OrderedDict()
        def wrapper2(*args, **kwargs):
            id = cls(*args, **kwargs).__dict__[unique]
            if not cls.instances.get(id, None):
                if len(cls.instances) < limit:
                    cls.instances[id] = cls(*args, **kwargs)
                else:
                    return list(cls.instances.values())[-1] if lookup == 'LAST' else list(cls.instances.values())[0]
            return cls.instances[id]
        return wrapper2
    return wrapper

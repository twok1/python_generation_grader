import functools
import re

def snake_case(attrs: bool=False):
    def to_snake(string):
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', string).lower()

    def decorator(cls):
        it = list(cls.__dict__.items())
        for attr, value in it:
            if not attr.startswith('__'):
                if callable(value) or attrs:
                    new_attr = to_snake(attr)
                    setattr(cls, new_attr, value)
                    delattr(cls, attr)
        return cls
    return decorator
    

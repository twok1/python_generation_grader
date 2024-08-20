from typing import Any


class NonNegativeObject:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)
            
    def __setattr__(self, name: str, value: Any) -> None:
        if isinstance(value, (int, float)) and value < 0:
            object.__setattr__(self, name, - value)
        else:
            object.__setattr__(self, name, value)
            
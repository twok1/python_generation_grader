from typing import Any


class AttrsNumberObject:
    def __init__(self, **kwargs) -> None:
        object.__setattr__(self, 'attrs_num', 1)
        for k, v in kwargs.items():
            self.__setattr__(k, v)
            
    def __setattr__(self, name: str, value: Any) -> None:
        if name in self.__dict__:
            object.__setattr__(self, 'attrs_num', self.attrs_num + 1)
        object.__setattr__(self, name, value)
        
    def __delattr__(self, name: str) -> None:
        object.__delattr__(self, name)
        object.__setattr__(self, 'attrs_num', self.attrs_num - 1)
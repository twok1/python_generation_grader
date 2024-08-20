from typing import Any


class DefaultObject:
    def __init__(self, default=None, **kwargs):
        self._default = default
        for k, v in kwargs.items():
            self.__setattr__(k, v)
            
    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)
        
    def __getattr__(self, name: str) -> Any:
        return self._default
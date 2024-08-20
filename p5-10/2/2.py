from typing import Any


class Row:
    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            object.__setattr__(self, k, v)
            
    def __setattr__(self, name: str, value: Any) -> None:
        if name in self.__dict__:
            raise AttributeError('Изменение значения атрибута невозможно')
        else:
            raise AttributeError('Установка нового атрибута невозможна')
        
    def __delattr__(self, name: str) -> None:
        if name in self.__dict__:
            raise AttributeError('Удаление атрибута невозможно')
        
    def __repr__(self) -> str:
        ret = ", ".join([f"{k}={repr(v)}" for k, v in self.__dict__.items()])
        return f"Row({ret})"
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Row):
            return tuple(self.__dict__.items()) == tuple(other.__dict__.items())
        return NotImplemented
        
    def __ne__(self, other) -> bool:
        if isinstance(other, Row):
            return tuple(self.__dict__.items()) != tuple(other.__dict__.items())
        return NotImplemented
    
    def __hash__(self) -> int:
        return hash(self.__repr__())

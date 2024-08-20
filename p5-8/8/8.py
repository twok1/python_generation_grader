from typing import Any


class ProtectedObject:
    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            object.__setattr__(self, k, v)
        
    def __getattribute__(self, name: str) -> Any:
        if name.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        else:
            return object.__getattribute__(self, name)
    
    def __setattr__(self, name: str, value: Any) -> None:
        if name.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        else:
            object.__setattr__(self, name, value)
        
    def __delattr__(self, name: str) -> None:
        if name.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        else:
            object.__delattr__(self, name)
        
        
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    print(user.login)
    print(user._password)
except AttributeError as e:
    print(e)
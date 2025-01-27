class MaxCallsException(Exception):
    pass

class LimitedTakes:
    def __set_name__(self, cls, attr):
        self._attr = attr

    def __init__(self, times):
        self._times = times

    def __get__(self, obj, cls):
        self._times -= 1
        if self._times < 0:
            raise MaxCallsException('Превышено количество доступных обращений')
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        else:
            raise AttributeError("Атрибут не найден")
    
    def __set__(self, obj, value):
        obj.__dict__[self._attr] = value

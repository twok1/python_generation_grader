class TypeChecked:
    def __set_name__(self, cls, attr):
        self._attr = attr

    def __init__(self, *args):
        self._types = args

    def __get__(self, obj, cls):    
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        else:
            raise AttributeError("Атрибут не найден")
    
    def __set__(self, obj, value):
        if type(value) in self._types:
            obj.__dict__[self._attr] = value
        else:
            raise TypeError("Некорректное значение")

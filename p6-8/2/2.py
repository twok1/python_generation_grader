class NonNegativeInteger:
    def __init__(self, attr, default=None):
        self._attr = attr
        self._default = default

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        elif self._default is not None:
            return self._default
        else:
            raise AttributeError("Атрибут не найден")

    def __set__(self, obj, value):
        if type(value) == int and value >= 0:
            obj.__dict__[self._attr] = value
        else:
            raise ValueError("Некорректное значение")

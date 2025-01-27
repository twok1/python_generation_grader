class Versioned:
    def __set_name__(self, cls, attr):
        self._attr = attr
        self._history = dict()

    def __get__(self, obj, cls):    
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        else:
            raise AttributeError("Атрибут не найден")
    
    def __set__(self, obj, value):
        self._history.setdefault(obj, [])
        self._history[obj].append(value)
        obj.__dict__[self._attr] = value

    def get_version(self, cls, n):
        return self._history[cls][n - 1]
    
    def set_version(self, cls, n):
        cls.__dict__[self._attr] = self._history[cls][n - 1]


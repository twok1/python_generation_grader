from abc import ABC, abstractmethod

class Validator(ABC):
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if not hasattr(obj, self.private_name):
            raise AttributeError("Атрибут не найден")
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass

class Number(Validator):
    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Устанавливаемое значение должно быть числом")
        if self.minvalue is not None and value < self.minvalue:
            raise ValueError(f"Устанавливаемое число должно быть больше или равно {self.minvalue}")
        if self.maxvalue is not None and value > self.maxvalue:
            raise ValueError(f"Устанавливаемое число должно быть меньше или равно {self.maxvalue}")

class String(Validator):
    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError("Устанавливаемое значение должно быть строкой")
        if self.minsize is not None and len(value) < self.minsize:
            raise ValueError(f"Длина устанавливаемой строки должна быть больше или равна {self.minsize}")
        if self.maxsize is not None and len(value) > self.maxsize:
            raise ValueError(f"Длина устанавливаемой строки должна быть меньше или равна {self.maxsize}")
        if self.predicate is not None and not self.predicate(value):
            raise ValueError("Устанавливаемая строка не удовлетворяет дополнительным условиям")
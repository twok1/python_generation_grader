from abc import ABC, abstractmethod


class Validator(ABC):
    def __set_name__(self, cls, attr):
        self._attr = attr

    def __set__(self, obj, value):
        if self.validate(value):
            self.__dict__[self._attr] = value

    def __get__(self, obj, cls):
        if self._attr in self.__dict__:
            return self.__dict__[self._attr]
        raise AttributeError('Атрибут не найден')

    @abstractmethod
    def validate(self, value):
        pass

class Number(Validator):
    def __init__(self, minvalue=None, maxvalue=None):
        self._minvalue = minvalue
        self._maxvalue = maxvalue
        super().__init__()

    def validate(self, value):
        if type(value) not in (int, float):
            raise TypeError('Устанавливаемое значение должно быть числом')
        if self._minvalue is not None and self._minvalue > value:
            raise ValueError(f'Устанавливаемое число должно быть больше или равно {self._minvalue}')
        if self._maxvalue is not None and self._maxvalue < value:
            raise ValueError(f'Устанавливаемое число должно быть меньше или равно {self._maxvalue}')
        return True
        
class String(Validator):
    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self._minsize = minsize
        self._maxsize = maxsize
        self._predicate = predicate
        super().__init__()

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError('Устанавливаемое значение должно быть строкой')
        if self._minsize is not None and self._minsize > len(value):
            raise ValueError(f'Длина устанавливаемой строки должна быть больше или равна {self._minsize}')
        if self._maxsize is not None and self._maxsize < len(value):
            raise ValueError(f'Длина устанавливаемой строки должна быть меньше или равна {self._maxsize}')
        if self._predicate and not self._predicate(value):
            raise ValueError('Устанавливаемая строка не удовлетворяет дополнительным условиям')
        return True

class Student:
    age = Number(18, 99)

print(Student.age.__class__)
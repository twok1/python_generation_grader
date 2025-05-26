from abc import ABC, abstractmethod


class Stat(ABC):
    def __init__(self, iterable=[]):
        self._iterable = list(i for i in iterable)

    def add(self, value):
        self._iterable.append(value)

    @abstractmethod
    def result(self):
        pass

    def clear(self):
        self._iterable.clear()

class MinStat(Stat):
    def result(self):
        if self._iterable:
            return min(self._iterable, default=None)
        
class MaxStat(Stat):
    def result(self):
        if self._iterable:
            return max(self._iterable, default=None)
    
class AverageStat(Stat):
    def result(self):
        if self._iterable:
            return sum(self._iterable) / len(self._iterable) if self._iterable else None
from abc import ABC, abstractmethod
from datetime import date

class Date(ABC):
    def __init__(self, year, month, day):
        self.date = date(year, month, day)

    @abstractmethod
    def format(self):
        pass

    def iso_format(self):
        return date.isoformat(self.date)

class USADate(Date):
    def format(self):
        return date.strftime(self.date, '%m-%d-%Y')
    
class ItalianDate(Date):
    def format(self):
        return date.strftime(self.date, '%d/%m/%Y')

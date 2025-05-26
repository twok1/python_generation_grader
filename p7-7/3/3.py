from abc import ABC, abstractmethod

class Paragraph(ABC):
    def __init__(self, length: int):
        self._length = length
        self._para = []

    def add(self, word: str):
        self._para.extend(word.split())

    @abstractmethod
    def end(self, side):
        while self._para:
            length = self._length
            fill = ' '
            what_print = ''
            while self._para and len(what_print) <= length - len(self._para[0]) - 1:
                what_print += ' ' + self._para.pop(0) if what_print else self._para.pop(0)
            print(f'{what_print:{fill}{side}{length}}' if side=='>' else what_print)

class LeftParagraph(Paragraph):
    def end(self):
        return super().end(side='<')
        
    
class RightParagraph(Paragraph):
    def end(self):
        return super().end(side='>')


from functools import total_ordering

@total_ordering
class RomanNumeral:
    def __init__(self, number) -> None:
        self.number = number
        self._roman = (
            ('I', 1),
            ('IV', 4),
            ('V', 5),
            ('IX', 9),
            ('X', 10),
            ('XL', 40),
            ('L', 50),
            ('XC', 90),
            ('C', 100),
            ('CD', 400),
            ('D', 500),
            ('CM', 900),
            ('M', 1000)
        )
        
    def __str__(self) -> str:
        return self.number
    
    def __int__(self):
        i = 0
        st = self.number
        num = 0
        while i < len(self._roman) and st:
            if st.rfind(self._roman[i][0]) >= 0 and st.rfind(self._roman[i][0]) == len(st) - len(self._roman[i][0]):
                num += self._roman[i][1]
                st = st[:len(st) - len(self._roman[i][0])]
                i = 0
            else:
                i += 1
        return num
    
    def num_to_roman(self, num):
        i = len(self._roman) - 1
        st = ''
        while i >=0:
            st += self._roman[i][0] * (num // self._roman[i][1])
            num %= self._roman[i][1]
            i -= 1
        return st
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, RomanNumeral):
            return self.__int__() == other.__int__()
        return NotImplemented
    
    def __ge__(self, other):
        if isinstance(other, RomanNumeral):
            return self.__int__() >= other.__int__()
        return NotImplemented
    
    def __add__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral(self.num_to_roman(self.__int__() + other.__int__()))
        return NotImplemented
        
    def __sub__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral(self.num_to_roman(self.__int__() - other.__int__()))
        return NotImplemented

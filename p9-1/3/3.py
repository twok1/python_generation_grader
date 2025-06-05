class CaesarCipher:
    def __init__(self, shift):
        self._shift = shift
        self.__charsA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.__charsB = "abcdefghijklmnopqrstuvwxyz"

    def encode(self, string):
        result = ''
        for sym in string:
            result += self.check_sym(sym)
        return result
        
    def decode(self, string):
        result = ''
        for sym in string:
            result += self.check_sym(sym, encode=-1)
        return result

    
    def check_sym(self, sym: str, encode: int = 1):
        for string in self.__charsA, self.__charsB:
            if sym in string:
                return string[(string.index(sym) + encode * self._shift) % 26]
        return sym

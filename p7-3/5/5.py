class SuperInt(int):
    def repeat(self, n=2):
        return SuperInt(f'{self}{str(abs(self)) * (n - 1)}')
    
    def to_bin(self):
        return f'{self:b}'
    
    def next(self):
        return SuperInt(self + 1)
    
    def prev(self):
        return SuperInt(self - 1)
    
    def __iter__(self):
        return iter(SuperInt(i) for i in str(self) if i.isdigit())

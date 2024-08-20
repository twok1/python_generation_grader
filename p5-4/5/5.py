class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self.value = value
        self.matrix = [[value for _ in range(cols)] for _ in range(rows)]
        
    def get_value(self, row, col):
        return self.matrix[row][col]
    
    def set_value(self, row, col, value):
        self.matrix[row][col] = value
        
    def __repr__(self) -> str:
        return f'Matrix({self.rows}, {self.cols})'
    
    def __str__(self) -> str:
        ret = ''
        ret = '\n'.join([' '.join(map(str, i)) for i in self.matrix])
        return ret
    
    def __pos__(self):
        return Matrix(self.rows, self.cols, self.value)
    
    def __neg__(self):
        res = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for k in range(self.cols):
                res.set_value(i, k, - self.get_value(i, k))
        return res
    
    def __invert__(self):
        res = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for k in range(self.cols):
                res.set_value(k, i, self.get_value(i, k))
        return res

    def __round__(self, digits=0):
        res = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for k in range(self.cols):
                res.set_value(i, k, round(self.get_value(i, k), digits))
        return res
    
class Calculator:
    def __call__(self, a, b, operation):
        if operation == '+':
            return a + b
        elif operation == '*':
            return a * b
        elif operation == '-':
            return a - b
        elif operation == '/':
            if b == 0:
                raise ValueError('Деление на ноль невозможно')
            return a / b
        
    
    
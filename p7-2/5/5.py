class Summator:
    m = 1

    def total(self, n):
        return sum(i ** self.m for i in range(1, n+1))
    
class SquareSummator(Summator):
    m = 2

    def total(self, n):
        return super().total(n)
    
class QubeSummator(Summator):
    m = 3
    def total(self, n):
        return super().total(n)
    
class CustomSummator(Summator):
    def __init__(self, m):
        self.m = m
    
    def total(self, n, m=1):
        return super().total(n)
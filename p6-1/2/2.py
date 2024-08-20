class DevelopmentTeam:
    def __init__(self) -> None:
        self.junior = []
        self.senior = []
        
    def add_junior(self, *args):
        self.junior += args
        
    def add_senior(self, *args):
        self.senior += args
        
    def __iter__(self):
        return iter(tuple((k, 'junior') for k in self.junior) + (tuple((k, 'senior') for k in self.senior)))
    
# k = DevelopmentTeam()
# k.add_junior('asf', 'bfd')
# print(list(iter(k)))
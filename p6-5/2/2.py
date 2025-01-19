class Greeter:
    def __init__(self, name) -> None:
        self.name = name
        
    def __enter__(self):
        print(f'Приветствую, {self.name}!')
        return self
        
    def __exit__(self, exc_type, exc_val, traceroute):
        print(f'До встречи, {self.name}!')
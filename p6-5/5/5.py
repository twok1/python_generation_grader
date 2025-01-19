class Reloopable:
    def __init__(self, file) -> None:
        self.file = file
        self.read = file.read().splitlines()
        
    def __enter__(self):
        return self.read
    
    def __exit__(self, *args, **kwargs):
        self.file.close()
        return None
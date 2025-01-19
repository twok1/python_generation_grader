class ReadableTextFile:
    def __init__(self, filename) -> None:
        self.filename = filename
        
    def __enter__(self):
        file = open(self.filename, 'r', encoding='utf-8')
        return map(str.strip, file.read().split('\n'))
    
    def __exit__(self, *args, **kwargs):
        return None
    
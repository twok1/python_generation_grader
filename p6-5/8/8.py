from io import TextIOWrapper

class WriteSpy:
    def __init__(self, file1: TextIOWrapper, file2: TextIOWrapper, to_close=False):
        self.files = (file1, file2)
        self.to_close = to_close

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.to_close:
            for f in self.files:
                if not f.closed:
                    f.close()
    
    def write(self, text) -> None:
        if not self.writable():
            raise ValueError("Файл закрыт или недоступен для записи")
        for f in self.files:
            f.write(text)

    def close(self) -> None:
        for f in self.files:
            f.close()

    def writable(self) -> bool:
        if any((f.closed for f in self.files)):
            return False
        return all((f.writable() for f in self.files))

    def closed(self) -> bool:
        return all((f.closed for f in self.files))

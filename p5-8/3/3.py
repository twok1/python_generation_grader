class Ord:
    def __getattr__(self, name):
        if len(name) == 1:
            return str(ord(name))
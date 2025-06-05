class ToStringMixin:
    def __repr__(self):
        cls = self.__class__.__name__
        args_str = [f"{k!r}: {v!r}" for k, v in self.__dict__.items()]
        if len(args_str) > 6:
            args_str = args_str[:6] + ['...']
        return f'{cls}({{{", ".join(args_str)}}})'
    

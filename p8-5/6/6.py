def auto_repr(args, kwargs):
    def decorator(cls):
        def repr(self):
            result = []
            if args:
                result.append(', '.join([f"{getattr(self, i)!r}" for i in args]))
            if kwargs:
                result.append(', '.join([f"{k}='{getattr(self, k)}'" for k in kwargs]))
            return f'{cls.__name__}({", ".join(result)})'
        cls.__repr__ = repr
        return cls
    return decorator

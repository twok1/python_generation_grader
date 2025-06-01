def add_attr_to_class(**kwargs):
    def decorator(cls):
        for attr, value in kwargs.items():
            setattr(cls, attr, value)
        return cls
    return decorator
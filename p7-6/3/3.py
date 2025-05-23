def get_method_owner(cls: object, method):
    for c in cls.__mro__:
        if method in c.__dict__:
            return c
    return None
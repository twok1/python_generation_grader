import json

def jsonattr(filename):
    with open(filename) as js:
        attrs = json.load(js)
    def decorator(cls):
        for attr, value in attrs.items():
            setattr(cls, attr, value)
        return cls
    return decorator
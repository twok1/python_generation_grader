class MROHelper:
    def len(cls):
        return len( cls.__mro__)
    
    def class_by_index(cls, n=0):
        return cls.__mro__[n]
    
    def index_by_class(child, parent):
        return child.__mro__.index(parent)

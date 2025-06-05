class AttributesMixin:
    def get_public_attributes(self):
        return [(i, k) for i, k in self.__dict__.items() if not i.startswith('_') and not callable(i)]
    
    def get_protected_attributes(self):
        cls = self.__class__.__name__
        return [(i, k) for i, k in self.__dict__.items() if i.startswith('_') and cls not in i and not callable(i)]

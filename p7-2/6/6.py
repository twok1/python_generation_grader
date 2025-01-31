class FieldTracker:
    _default_attrs = {}
    _changed_attrs = {}

    def base(self, attr):
        return self._default_attrs[attr]

    def has_changed(self, attr):
        return attr in self._changed_attrs

    def changed(self):
        return {i: self._default_attrs[i] for i in self._changed_attrs}

    def save(self):
        self._default_attrs.update(self._changed_attrs)
        self._changed_attrs = dict()

    def __setattr__(self, name, value):
        if name in self.fields and name not in self._default_attrs:
            self._default_attrs[name] = value
            self.__dict__[name] = value
        elif name in self._default_attrs and self._default_attrs[name] != value:
            self.__dict__[name] = value
            self._changed_attrs[name] = value
        elif name not in self._default_attrs:
            self.__dict__[name] = value
        elif name in self._default_attrs and self._default_attrs[name] == value:
            self._changed_attrs.pop(name)

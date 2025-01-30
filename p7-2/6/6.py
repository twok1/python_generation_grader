class FieldTracker:
    def __init__(self, *args):
        self._default_attrs = dict()
        self._changed_attrs = dict()

    def base(self):
        pass

    def has_changed(self):
        pass

    def changed(self):
        pass

    def save(self):
        pass
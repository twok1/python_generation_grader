class HtmlTag:
    level = -1
    
    def __init__(self, tag, inline=False):
        self.tag = tag
        if inline:
            self.inline = ''
        else:
            self.inline = '\n'

    def __enter__(self):
        type(self).level += 1
        line = f"{'  ' * type(self).level}<{self.tag}>"
        print(line, end=self.inline)
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        type(self).level -= 1
        level_up = - type(self).level
        if self.inline:
            level_up = 1
        print(f"{'  ' * (type(self).level  + level_up)}</{self.tag}>")
        return True

    def print(self, text):
        level_up = - type(self).level
        if self.inline:
            level_up = 1
        line = f"{'  ' * (type(self).level + level_up)}{text}"
        print(line, end=self.inline)

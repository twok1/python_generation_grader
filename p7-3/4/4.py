class TitledText(str):
    def __new__(cls, content, text_title):
        instanse = super().__new__(cls, content)
        instanse.title = lambda: text_title
        return instanse

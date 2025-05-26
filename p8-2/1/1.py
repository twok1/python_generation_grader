from enum import Enum

class HTTPStatusCodes(Enum):
    CONTINUE = 100
    OK = 200
    USE_PROXY = 305
    NOT_FOUND = 404
    BAD_GATEWAY = 502

    def info(self):
        return (self.name, self.value)
    
    def code_class(self):
        groups = ('информация', 'успех', 'перенаправление', 'ошибка клиента', 'ошибка сервера')
        codes = dict(zip(HTTPStatusCodes, groups))
        return codes[self]

        if self.value in range(100, 200):
            return 'информация'
        if self.value in range(200, 300):
            return 'успех'
        if self.value in range(300, 400):
            return 'перенаправление'
        if self.value in range(400, 500):
            return 'ошибка клиента'
        if self.value in range(500, 600):
            return 'ошибка сервера'
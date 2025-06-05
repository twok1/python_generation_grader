import datetime

class LoggerMixin:
    def log(self, level, text):
        date = datetime.datetime.strftime(datetime.datetime.now(), '%d.%m.%Y %H:%M:%S')
        print(f'[{date}] - {level} - {self.__class__.__name__}: {text}')

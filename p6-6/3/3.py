from contextlib import contextmanager
from io import StringIO


@contextmanager
def safe_write(filename):
    f = None
    temp = StringIO()
    try:
        yield temp
        data = temp.getvalue()
        f = open(filename, 'w')
        f.write(data)
    except Exception as e:
        print(f'Во время записи в файл было возбуждено исключение {type(e).__name__}')
    finally:
        if f:
            f.close()

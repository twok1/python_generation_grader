from contextlib import contextmanager


@contextmanager
def safe_open(filename, mode='r'):
    file = None
    try:
        file = open(filename, mode=mode)
        yield (file, None)
        file.close()
    except Exception as e:
        yield (None, e)

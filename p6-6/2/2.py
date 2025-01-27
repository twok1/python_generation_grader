from contextlib import contextmanager
import sys


@contextmanager
def reversed_print():
    old_stdout = sys.stdout.write
    sys.stdout.write = lambda x: old_stdout(x[::-1])
    yield 
    sys.stdout.write = old_stdout

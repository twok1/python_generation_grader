import sys

class UpperPrint:
    def __init__(self) -> None:
        self.normal_stdout = sys.stdout.write
        pass
        
    def __enter__(self):
        # return lambda text: self.normal_stdout(text.upper())
        sys.stdout.write = lambda text: self.normal_stdout(text.upper())
    
    def __exit__(self, *args, **kwargs):
        sys.stdout.write = self.normal_stdout
        return None
        
        
        
# import sys

# class RedirectedStdout:
#     def __init__(self):
#         pass

#     def __enter__(self):
#         self.standard_output = sys.stdout
#         sys.stdout = self.new_output

#     def __exit__(self, exc_type, exc_value, traceback):
#         sys.stdout = self.standard_output 
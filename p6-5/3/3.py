class Closer:
    def __init__(self, obj):
        self.obj = obj
        
    def __enter__(self):
        self.closed = False
        return self.obj
        
    def __exit__(self, *args, **kwargs):
        try:
            self.obj.close()
            self.closed = True
        except:
            print('Незакрываемый объект')
            
            
# with Closer(5) as i:
#     i += 1
    
# print(i)
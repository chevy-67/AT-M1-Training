class Model:
    def __init__(self,name):
        self.name = name
    def model_name(self):
        return self.name

def Max(a:int, b:int)->int:
     if a>b:
         return a
     return b

PI = 3.14
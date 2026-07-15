class Person:
    def __init__(self,name):
        self._name = name
    
    @property
    def name(self):
        return self._name


p1 = Person("Akil")
print(p1.name)
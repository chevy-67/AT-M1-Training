class A:
    def __init__(self,name):
        self.name = name
    # def __str__(self):
    #     return f"{self.name} is printing"
    def __len__(self):
        return len(self.name)
    def __repr__(self):
        return f"{type(self).__name__}(name={self.name})"

a = A("Bala")
print(a)
print(len(a))
class A:
    def __init__(self):
        self.name = "ken"

class B:
    def __init__(self):
        self.A = A()

b = B()
print(b.A.name)

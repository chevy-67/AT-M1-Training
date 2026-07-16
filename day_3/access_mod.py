class A:
    def __init__(self):
        self._name = 'abi'

class B:
    def __init__(self):
        self.__balance = 1000

a = A()
print(a._name)

b = B()
b._B__balance = 10
print(b._B__balance)
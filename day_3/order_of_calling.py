class A:
    def call(self):
        print("From A")

class B:
    def call(self):
        print("From B")

class C(B,A):
    # def call(self):
    #     print("From C")
    pass

c = C()
c.call()